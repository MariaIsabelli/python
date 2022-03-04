# python
##Estudos com a linguagem python<br/>
##Biblioteca NLTK<br/>
**import nltk**<br/>
O NLTK foi chamado de “uma ferramenta maravilhosa para ensinar e trabalhar em linguística computacional usando Python” e “uma biblioteca incrível para brincar com linguagem natural”.
Processamento de linguagem natural com Python fornece uma introdução prática à programação para processamento de linguagem. Escrito pelos criadores do NLTK, ele orienta o leitor pelos fundamentos da escrita de programas Python, trabalhando com corpora, categorizando texto, analisando estrutura linguística e muito mais. A versão online do livro foi atualizada para Python 3 e NLTK 3. (A versão original do Python 2 ainda está disponível em https://www.nltk.org/book_1ed .)

##Biblioteca pandas:<br/>
Pandas também é o nome de uma biblioteca poderosa para manipulação e análise de dados utilizando a linguagem Python. Por esse motivo, se você pretende trabalhar na área de análise e ciência de dados com essa linguagem de programação precisa conhecer essa biblioteca e as ferramentas que ele oferece!
Como mencionado anteriormente, Pandas é uma biblioteca para uso em Python, open-source e de uso gratuito (sob uma licença BSD), que fornece ferramentas para análise e manipulação de dados.
De acordo com o próprio criador dessa biblioteca, Wes McKinney, o nome Pandas é derivado de panel data (dados em painel), um termo de econometria para conjuntos de dados estruturados. O surgimento da biblioteca, no início de 2008, começou devido a insatisfação de McKinney de obter uma ferramenta de processamento de dados de alto desempenho, com recursos flexíveis de manipulação de planilhas e de banco de dados relacionais.


##Biblioteca FER:<br/>
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
