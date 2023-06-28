import { Kafka } from "kafkajs";

async function launchCfaracterPusher() {
  const kafka = new Kafka({
    clientId: "my-app",
    brokers: ["localhost:29092"],
  });

  const consumer = kafka.consumer({ groupId: "test-group" });

  await consumer.connect();
  await consumer.subscribe({ topic: "new_character", fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      const value = JSON.parse(JSON.parse(message.value.toString()));
      console.log(value);
      console.log(value.name);
    },
  });
}
launchCfaracterPusher();
