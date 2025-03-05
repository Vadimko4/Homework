import logging

# Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='application.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

# Создаем логеры для различных компонентов программы
utils_logger = logging.getLogger('app.utils')
masks_logger = logging.getLogger('app.masks')