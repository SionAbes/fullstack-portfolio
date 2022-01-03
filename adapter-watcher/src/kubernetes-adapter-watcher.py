from typing import List

import requests
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from src.models.adapters import Adapter
from src.settings import Settings, get_settings


def login_to_master_api(settings: Settings) -> str:
    data = {
        "grant_type": None,
        "username": settings.MASTER_API_USERNAME,
        "password": settings.MASTER_API_PASSWORD,
        "scope": None,
        "client_id": None,
        "client_secret": None,
    }
    response = requests.post(f"{settings.MASTER_API_BASE}/auth/login", data=data)
    return response.json()["access_token"]


def get_adapters(settings: Settings, token: str) -> List[Adapter]:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{settings.MASTER_API_BASE}/adapters",
        headers=headers,
    )
    if response.status_code != 200:
        raise Exception("api is currently down")
    return [Adapter(**adapter) for adapter in response.json()]


def create_adapter_cronjob(
    *,
    configuration,
    cronjob_name: str,
    cronjob_schedule: str,
    adapter_name: str,
    image: str,
):
    with client.ApiClient(configuration) as api_client:
        api_instance = client.BatchV1Api(api_client)
        namespace = "adapters"
        body = client.V1CronJob(
            api_version="batch/v1",
            kind="CronJob",
            metadata=client.V1ObjectMeta(
                name=cronjob_name,
            ),
            spec=client.V1CronJobSpec(
                concurrency_policy="Forbid",
                schedule=cronjob_schedule,
                successful_jobs_history_limit=0,
                failed_jobs_history_limit=0,
                job_template=client.V1JobTemplateSpec(
                    spec=client.V1JobSpec(
                        backoff_limit=0,
                        template=client.V1PodTemplateSpec(
                            spec=client.V1PodSpec(
                                containers=[
                                    client.V1Container(
                                        image=image,
                                        image_pull_policy="Always",
                                        name=adapter_name,
                                        volume_mounts=[
                                            client.V1VolumeMount(
                                                mount_path=f"/usr/src/{adapter_name}/config.yaml",
                                                name="config-vol",
                                                sub_path="config.yaml",
                                            )
                                        ],
                                    )
                                ],
                                image_pull_secrets=[
                                    client.V1LocalObjectReference(
                                        name="githubcontainerregistry",
                                    )
                                ],
                                restart_policy="Never",
                                volumes=[
                                    client.V1Volume(
                                        config_map=client.V1ConfigMapVolumeSource(
                                            default_mode=420, name=adapter_name
                                        ),
                                        name="config-vol",
                                    )
                                ],
                            )
                        ),
                    )
                ),
            ),
        )
        try:
            api_instance.create_namespaced_cron_job(namespace, body, pretty="true")
        except ApiException as e:
            print(
                "Exception when calling BatchV1Api->create_namespaced_cron_job: %s\n"
                % e
            )

    return


def main():

    settings = get_settings()
    token = login_to_master_api(settings=settings)
    adapters = get_adapters(settings=settings, token=token)

    if settings.ENV == "local":
        configuration = config.load_kube_config()
    else:
        configuration = config.load_incluster_config()

    for adapter in adapters:

        adapter_name = adapter.adapter_name.replace("_", "-")  # convert to kebab case
        cronjob_schedule = adapter.cron_expression
        cronjob_name = f"{adapter.user_id}-{adapter_name}-cronjob"
        image = f"{adapter_name}:latest"

        create_adapter_cronjob(
            configuration=configuration,
            cronjob_name=cronjob_name,
            cronjob_schedule=cronjob_schedule,
            adapter_name=adapter_name,
            image=image,
        )


if __name__ == "__main__":
    main()
