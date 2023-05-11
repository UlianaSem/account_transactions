from datetime import date


class Operation:
    """Описывает свойства операции"""
    def __init__(self, transaction_id, operation_date, transfer_state, operation_amount, transfer_description,
                 payment_to, payment_from=None):
        """
        Инициализируем поля
        :param transaction_id: id транзакциии
        :param operation_date: информация о дате совершения операции
        :param transfer_state: статус перевода
        :param operation_amount: сумма операции и валюта
        :param transfer_description: описание типа перевода
        :param payment_to: куда
        :param payment_from: откуда (может отсутстовать)
        """
        self.transaction_id = transaction_id
        self.operation_date = operation_date
        self.transfer_state = transfer_state
        self.operation_amount = operation_amount
        self.transfer_description = transfer_description
        self.payment_to = payment_to
        self.payment_from = payment_from

    def __repr__(self):
        """
        Выводит представление об операции:
        """
        return f'Operation ({self.transaction_id}, "{self.operation_date}", "{self.transfer_state}", ' \
               f'{self.operation_amount}, "{self.transfer_description}", "{self.payment_from}", "{self.payment_to}")'

    def get_encrypted_to_number(self):
        """
        Скрывает номер исходящей(его) карты/ счета
        :return: строка с зашифрованным номером
        """
        payment_to_list = self.payment_to.split()
        if payment_to_list[0] == 'Счет':
            encrypted_to = payment_to_list[0] + ' **' + payment_to_list[1][-4:]
        else:
            encrypted_to = ' '.join(payment_to_list[:-1]) + ' ' + payment_to_list[-1][:4] + ' ' +\
                           payment_to_list[-1][4:6] + '** **** ' + payment_to_list[-1][-4:]

        return encrypted_to

    def get_encrypted_from_number(self):
        """
        Скрывает номер входящей(его) карты/ счета
        :return: строка с зашифрованным номером
        """
        if self.payment_from is None:
            encrypted_from = 'Нет данных об исходящем счете'
        else:
            payment_from_list = self.payment_from.split()
            if payment_from_list[0] == 'Счет':
                encrypted_from = payment_from_list[0] + ' **' + payment_from_list[1][-4:]
            else:
                encrypted_from = ' '.join(payment_from_list[:-1]) + ' ' + payment_from_list[-1][:4] + ' ' +\
                                 payment_from_list[-1][4:6] + '** **** ' + payment_from_list[-1][-4:]

        return encrypted_from

    def format_date(self):
        """
        Приводит дату к формату ДД.ММ.ГГГГ
        :return: дата в формате ДД.ММ.ГГГГ
        """
        date_for_formatting = date.fromisoformat(self.operation_date.split('T')[0])
        formatted_date = date_for_formatting.strftime('%d.%m.%Y')

        return formatted_date

    def build_response(self):
        """
        Строит ответ в нужном формате
        :return: <дата перевода> <описание перевода>
                <откуда> -> <куда>
                <сумма перевода> <валюта>
        """
        return f'''{self.format_date()} {self.transfer_description}
{self.get_encrypted_from_number()} -> {self.get_encrypted_to_number()}
{self.operation_amount['amount']} {self.operation_amount['currency']['name']}'''
