# python
Estudos com a linguagem python
#Biblioteca FER: 
A Biblioteca de Reconhecimento de Expressão Facial é desenvolvida por Justin Shenk . Esta biblioteca requer dependências OpenCV>=3.2 e Tensorflow>=1.7.0 instaladas no sistema. Os rostos são detectados usando o classificador Haar Cascade do OpenCV. Para obter mais informações e o código-fonte da Biblioteca FER, você pode visitar a página GitHub da FER aqui.

 Configurando nosso código!
Para este artigo, você pode usar um editor de código online chamado Repl.it ou pode usar seu editor de código favorito. Pode ser instalado através  

pip:`$ pip install fer`
import cv2
 
from fer import FER
 
import matplotlib.pyplot as plt
 
import matplotlib.image as mpimg
O código acima diz que:

Importe ` cv2` completo , comumente conhecido como biblioteca Open CV. Ele nos fornece várias soluções de visão computacional. Usaremos esta biblioteca principalmente para leitura e manipulação de imagens. Você pode ler mais sobre `Biblioteca Open Cv` nos Documentos OpenCV 
Importe a função `FER` da biblioteca `fer` . Esta é a biblioteca principal que usaremos neste workshop.
Adicione o módulo ` matplotlib.pyplot ` como ` plt `. Isso nos ajudará a traçar gráficos
Inclua o módulo `matplotlib.image` como ` mpimg` . O matplotlib.image da biblioteca matplotlib  é usado para plotar a imagem no gráfico com os eixos `x` e `y
