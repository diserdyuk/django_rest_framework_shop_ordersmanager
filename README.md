# django_rest_framework_shop_ordersmanager

Реализовать систему для управлением заказами в магазине техники. 
Представьте, что ваш клиент хочет автоматизировать свой бизнес в магазине техники, 
и вам нужно внедрить серверную часть для этой автоматизации.


ТЕСТОВОЕ ЗАДАНИЕ
В системе задействованы следующие участники:
-Продавец-консультант
-Кассир
-Бухгалтер

Типичный вариант использования:
-кассир получает заказ от клиента. В одном заказе может быть только один продукт
--добавляет этот заказ в базу данных
-продавец-консультант может видеть созданный заказ
--обрабатывает его и затем изменяет его статус на «выполнено»

После этого:
-кассир может сгенерировать счет
-принять оплату от клиента и изменить статус заказа на «оплачен»
В любое время бухгалтер может видеть все заказы, их статусы, дату, скидку и тд.
Бухгалтер указывает промежуток дат по которым необходимо вывести данные о заказах.
Например: показать все заказы с 01.07.2019 до 31.07.2019

Продукты имеют название, цену и дату создания. 
В системе должен быть реализован механизм начисления скидок для товаров. 
Если дата создания продукта больше одного месяца от текущей даты, 
то на него должна быть предоставлена скидка 20%.

Счет должен содержать информацию о товаре (название, цена) и дату создания заказа и
дату создания счета.

ТРЕБОВАНИЯ К ОФОРМЛЕНИЮ
-Система должна быть выполнена в виде REST API (либо GraphQL)
-В проекте должны быть фикстуры для продуктов
-Необходимо предоставить Postman коллекцию (GraphQL Playground) со всеми ендпоинтами, 
либо документацию к реализованным endpoints в любом удобном для вас виде
-Код должен соответствовать общепринятым стилевым и организационным
стандартам действующим для выбранных вами языков и технологий
-По возможности код должен сопровождаться разумными комментариями,
юнит-тестами, прочими инструкциями