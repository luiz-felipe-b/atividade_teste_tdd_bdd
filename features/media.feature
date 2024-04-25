Feature: Fazer a média entre dois números
    Scenario: Realizar uma média simples
        Given eu tenho dois números inteiros: 5 e 7
        When eu faço a média dos dois números inteiros
        Then o resultado deve ser 6

        Given eu tenho dois números inteiros: 4 e 4
        When eu faço a média dos dois números inteiros
        Then o resultado deve ser 4