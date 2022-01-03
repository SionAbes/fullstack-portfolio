from kubernetes import client, config
from kubernetes.client.rest import ApiException
from src.settings import get_settings


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
    cronjob_schedule = "0 * * * *"
    cronjob_name = "cronjob-name"
    image = "image_name"
    adapter_name = "adapter-name"

    settings = get_settings()

    if settings.ENV == "local":
        configuration = config.load_kube_config()
    else:
        configuration = config.load_incluster_config()

    create_adapter_cronjob(
        configuration=configuration,
        cronjob_name=cronjob_name,
        cronjob_schedule=cronjob_schedule,
        adapter_name=adapter_name,
        image=image,
    )


if __name__ == "__main__":
    main()
