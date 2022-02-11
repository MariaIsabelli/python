from fer import FER
import matplotlib.pyplot as plt 
img = plt.imread("/content/download.jpg")
detector = FER(mtcnn=True)
sentimentos = (detector.detect_emotions(img))
top_sentimento = (detector.top_emotion(img))

print(f"Brava: {sentimentos[0]['emotions']['angry']}")
print(f"Disgosto: {sentimentos[0]['emotions']['disgust']}")
print(f"Medo: {sentimentos[0]['emotions']['fear']}")
print(f"Feliz: {sentimentos[0]['emotions']['happy']}")
print(f"Triste: {sentimentos[0]['emotions']['sad']}")
print(f"Surpreso: {sentimentos[0]['emotions']['surprise']}")
print(f"Neutro: {sentimentos[0]['emotions']['neutral']}")

def getTopSentimento(sentimento):
  emocao = sentimento[0]
  if(emocao == 'angry'):
    return 'bravo'
  elif(emocao == 'disgust'):
    return 'com disgosto'
  elif(emocao == 'fear'):
      return 'com medo'
  elif(emocao == 'happy'):
    return 'feliz'
  elif(emocao == 'sad'):
    return 'triste'
  elif(emocao == 'surprise'):
    return 'surpreso'
  elif(emocao == 'neutral'):
    return 'neutro'
  else:
    'ERRO(Não foi possivel identificar emoção)'


print(f"Está provavelmente: {getTopSentimento(top_sentimento)}")
plt.imshow(img)
