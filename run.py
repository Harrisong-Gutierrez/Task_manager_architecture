# run.py
from app import create_app

import logging

from app.infrastructure.config import AlchemyConfig

# Configura logging básico
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = create_app(AlchemyConfig)

if __name__ == '__main__':
    try:
        # Inicia la aplicación en modo desarrollo
        app.run(
            host='0.0.0.0', 
            port=5000, 
            debug=True,
            use_reloader=True
        )
    except Exception as e:
        logging.error(f"Error al iniciar la aplicación: {str(e)}")
        raise