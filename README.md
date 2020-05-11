# A3_RoboticaComputacional

<h2>Informações Gerais</h2>

<h3>Engenharia de Computação Insper - Robótica Computacional 2020.1</h3>

<h3>Alunos:</h3>
<ul>
  <li><a href=https://www.linkedin.com/in/enrico-damiani-125527196/>Enrico Francesco Damiani</a></li>
  <li><a href=https://www.linkedin.com/in/marcosvinis28/>Marcos Vinícius da Silva</a></li>
</ul>

<h3>Professor:</h3> 
<ul>
  <li><a href=https://www.linkedin.com/in/fabiodemiranda/>Me. Fabio Roberto de Miranda</a></li>
</ul>

<h2>Informações da Atividade</h2>

<h3>Objetivos:</h3>

<h4>Parte 1 - Ponto de Fuga</h4>
<p>
Robôs que trabalham dentro de prédios precisam saber seguir corredores. Uma das maneiras de fazer isso é o robô alinhar o centro de sua câmera ao ponto de fuga do corredor, para que sua trajetória seja aproximadamente paralela às paredes do mesmo. O ponto de fuga é aquele para o qual as retas paralelas parecem convergir.
</p>

<h4>Parte 2 - Executar dois exemplos</h4>
<p>
Há três exemplos: mobilenet_detection, yolov3_detection e tracking. Os dois primeiros são reconhecedores de objetos, e o último é de rastreamento. Um dos arquivos abaixo precisa ser baixado e salvo nas pasta yolov3_detection/yolov3-coco.
https://www.dropbox.com/s/013ogt2bhwfzxwb/yolov3.weights?dl=0 ou https://pjreddie.com/media/files/yolov3.weights

Atenção: Vamos rodar a Yolo só por importância "histórica". Depois de rodar o demos, estude o notebook Demo_Imagenet.ipynb
</p>

<h4>Parte 3 - Identificar Objeto</h4>
<p>
Use o projeto mobilenet_detection para basear seu código. Neste projeto, escolha uma categoria de objetos que o reconhecedor reconhece. Diga aqui qual foi sua escolha. Implemente a seguinte funcionalidade: sempre que o objeto identificado em (2) estiver presente por mais que 5 frames seguidos, desenhe um retângulo fixo ao redor dele.
</p>

<h4>Parte 4 - Simulador</h4>
<p>
Rode o simulador do Turtlebot (use o Waffle). Veja o guia em ../guides/simulador_ros.md. Documente aqui as linhas necessárias para teleop e para abrir o Rviz. Faça um screenshot do seu simulação em execução.
</p>

<h4>Parte 5 - Robô Quadrado</h4>
<ul>
  <li>Usando o simulador, crie um código que faça o robô fazer uma trajetória que aproxima um quadrado.</li>
  <li><a href=https://youtu.be/x2kTETlEfHU>Vídeo comprovando o resultado da parte 5 da atividade 3</li>
</ul>

<h4>Parte 6 - Robô Indeciso</h4>
<p>
Usando o simulador e o LIDAR simulado, faça um robô avançar quando o obstáculo bem à sua frente estiver a menos de 1.0m e recuar quando estiver a mais de 1.02 m. Baseie-se no código le_scan.py e roda.py, desenvolvidos durante o tutorial.
</p>
