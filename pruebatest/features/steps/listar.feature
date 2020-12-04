Feature: listar los proctuctos productos

    Scenario Outline: listar
    Given <nombre> para listar los productos
    When se lista los productos
    Then el <precio> del producto es correcto

    Examples:
        | nombre  | precio|
        |Manzana  |   12  |
        |Pera     |   30  |
        |Piña     |   52  |
        |Platano  |   38  |
        |Aguacate |  100  |