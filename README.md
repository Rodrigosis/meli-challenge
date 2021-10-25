## Setup

- Crie a imagem docker:
  ```bash
  sudo docker-compose build
  ```
- Suba os containers:
  ```bash
  sudo docker-compose up
  ```
- Realizar chamadas utilizando interface swagger:
  ```bash
  http://0.0.0.0:8000/docs
  ```

## Testing
- rodar tests e verificação de tipagem e mau cheiro de código:
    ```bash
    sudo docker-compose exec app bash ./bin/ci.sh
    ``` 
- rodar somente verificação de tipagem e mau cheiro de código:
    ```bash
    sudo docker-compose exec app bash ./bin/lint.sh
    ``` 
- rodar somente tests:
    ```bash
    sudo docker-compose exec app bash ./bin/test.sh
    ``` 


## Arquitetura
```console
src/
├── application/  # Camada que se comunica com o mundo externo e manipula a camada domain.
├── domain/  # Camada onde os dados recebidos do mundo externo são processados.
└── infra/  # Camada onde ficam elementos externos de infraestrutura que ajudam o serviço a funcionar (banco de dados, cache, etc).