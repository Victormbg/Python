import Algorithmia


input = {
  "image": "https://scontent.fsdu6-1.fna.fbcdn.net/v/t1.0-9/45254675_1581181962028083_1037032833010368512_n.jpg?_nc_cat=105&_nc_eui2=AeGlAxvt_BIclCQ3nuutR8YqCdWFNGAvMSM-hR9eTWoz0IyJy5vC31Le8GjCBO_B6q6h3Ho21XHv7IZwlnpGptdYnCgwO8yGHh6GE9Hpsacf4A&_nc_ht=scontent.fsdu6-1.fna&oh=433e91d0d1cedfbeb7816fb562055928&oe=5C42165B",
  "output": "data://.algo/deeplearning/ObjectDetectionCOCO/temp/suit_and_tie.png",
  "min_score": 0.7,
  "model": "ssd_mobilenet_v1"
}

client = Algorithmia.client('simUZVqt38ilLla2/p89MxMuj9p1')
algo = client.algo('deeplearning/ObjectDetectionCOCO/0.2.1')
print(algo.pipe(input).result)
