import faust

app = faust.App("myapp", broker="kafka://localhost:9093")
topic = app.topic("metrics")


@app.agent(topic)
async def hello(messages):
    async for message in messages:
        print(f"Received {message}")
