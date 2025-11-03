from kafka import KafkaProducer
from PollResponseAPI import PollResponseAPI
import time
import json

# kafka topicname 
topic_name = "live_poll_responses"

# creating kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# pollresponce API object
api = PollResponseAPI()

# print("Sending poll responses...\n")

try:
    while True:
        # generate a fake poll response
        poll_data = json.loads(api.poll_response_api())
        print("produced:", poll_data)

        # send it to kafka topic 
        producer.send(topic_name, poll_data)

        # wait for 3 seconds before sending next one 
        time.sleep(2)

except KeyboardInterrupt:
    print("\n producer stopped by user!!")

finally:
    producer.close()