#!/bin/bash

# Установка PYTHONPATH на папку src (или другую, если нужно)
export PYTHONPATH=$(pwd)/src

"Запуск тестов"
# Запуск pytest над папкой tests
pytest tests/
