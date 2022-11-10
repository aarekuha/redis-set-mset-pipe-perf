#### Анализ производительности методов добавления записи Redis
##### Один экземпляр Redis
###### Запуск
```bash
    docker-compose -f docker-compose-single.yml up -d
    python -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

    python single_test.py
```
###### Результаты (сек на 1000 записей)
```
    SET: 0.088
    MSET: 0.002
    PIPE: 0.009
```

##### Кластер из 6 нод
###### Запуск
```bash
    docker-compose -f docker-compose-cluster.yml up -d
    python -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt

    python cluster_test.py
```
###### Результаты (сек на 1000 записей)
```
    SET: 0.080
    MSET: 0.071
    PIPE: 0.010
```
