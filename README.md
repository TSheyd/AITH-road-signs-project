# AITH-road-signs-project
AI Talent Hub Deep Learning Practice Course - road signs detection

# Данные для обучения
Для обучения были взяты данные из двух датасетов:
1) Traffic and Road Signs Computer Vision Project [1]
2) Russian-traffic-signs-recognition Computer Vision Project [2]
   
<img width="714" alt="Снимок экрана 2023-11-28 в 17 11 39" src="https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/52c6c4cd-ccf4-4296-8cec-4c21ece37836">

# Обучение моделей
 **Exp 1**

Для реализации детектирования знаков было принято использовать модель архитектуры YOLO, а конкретно семейство YOLOv8, так как модели показывают хорошие результыт при работе в realtime.

Так как модель будет работать на мобильных устройствах, то было принято решение использовать модель yolov8 nano.

Первая модель была обучена на датасете Traffic and Road Signs Computer Vision Project. Полученные метрики представлены на графиках ниже.

![F1_curve](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/9ba22f71-4066-4088-9e86-695efb340b86)
![val_batch0_labels](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/988320e4-dfc0-4306-94f1-30172cf064ee)

При этом модель совершенно не справлялась при работе с реальными данными:
![Снимок экрана 2023-11-28 в 17 18 30](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/bb2a9fab-25ba-4139-b457-4b2e24343adf)

Из-за этого было принято решение провести еще два эксперимента.

 **Exp 2**

 Модель была обучена с нуля на наборе данных Russian-traffic-signs-recognition Computer Vision Project. Показатель F1 Score и PR-кривая предоставлен на графике ниже.
 ![F1_curve](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/000ad0cb-8e2f-42d3-820a-929d0fe3113a)

 ![PR_curve](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/46de924f-af37-4e39-8137-e5e2f05cd67a)

 При более низких метриках можно видеть, что модель заметно лучше справлялась с реальными данными.
 ![val_batch2_labels](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/8bdf61f3-e21e-4847-b6fa-6a5e2f6bc578)

 Также стоит отметить, что невысокий показатель f1 связан с усреднением его по всем классам. 

  **Exp 3**

  Модель полученная в эксперименте 1 была дообучена на данных из эксперимента 2.
  ![F1_curve](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/35e5a230-c8d3-4ed0-9178-5b74dd737363)
![PR_curve](https://github.com/TSheyd/AITH-road-signs-project/assets/92350053/7aaf1d38-1732-45e3-92f7-bd9571b08fc3)

  За отсутсвием значимых изменений между экспериментами 2 и 3 было принято использовать модель из второго эксперимента.

 # Ссылки и источники
 1) https://universe.roboflow.com/usmanchaudhry622-gmail-com/traffic-and-road-signs
 2) https://universe.roboflow.com/mguogareva/russian-traffic-signs-recognition

