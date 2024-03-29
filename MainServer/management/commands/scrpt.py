from django.core.management.base import BaseCommand
from django.db import transaction
from MainServer.models import FuelStation, Fuel, FuelPrices


class Command(BaseCommand):
    help = 'Load JSON data into Django models'

    def handle(self, *args, **kwargs):
        json_data = [
            {
                "Address": "г. Санкт-Петербург, Богатырский проспект, 23",
                "Station_ID": 1,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.09,
                        "AmountOfFuel": 43360
                    },
                    {
                        "Name": "95",
                        "Price": 47.67,
                        "AmountOfFuel": 50149
                    },
                    {
                        "Name": "98",
                        "Price": 56.2,
                        "AmountOfFuel": 17943
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.5,
                        "AmountOfFuel": 30075
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Витебский проспект, 9к2 литера А",
                "Station_ID": 2,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.49,
                        "AmountOfFuel": 56531
                    },
                    {
                        "Name": "95",
                        "Price": 47.85,
                        "AmountOfFuel": 81209
                    },
                    {
                        "Name": "98",
                        "Price": 56.09,
                        "AmountOfFuel": 49249
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.69,
                        "AmountOfFuel": 82789
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Витебский проспект, 153",
                "Station_ID": 3,
                "data": [
                    {
                        "Name": "92",
                        "Price": 42.4,
                        "AmountOfFuel": 79325
                    },
                    {
                        "Name": "95",
                        "Price": 44.85,
                        "AmountOfFuel": 83131
                    },
                    {
                        "Name": "98",
                        "Price": 51.6,
                        "AmountOfFuel": 30789
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 51.8,
                        "AmountOfFuel": 88761
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Витебский проспект, 157",
                "Station_ID": 4,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.2,
                        "AmountOfFuel": 56700
                    },
                    {
                        "Name": "95",
                        "Price": 46.7,
                        "AmountOfFuel": 32636
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 10652
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.9,
                        "AmountOfFuel": 60992
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Выборгская набережная, 57",
                "Station_ID": 5,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.83,
                        "AmountOfFuel": 29172
                    },
                    {
                        "Name": "95",
                        "Price": 47.7,
                        "AmountOfFuel": 47850
                    },
                    {
                        "Name": "98",
                        "Price": 53.15,
                        "AmountOfFuel": 8886
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.4,
                        "AmountOfFuel": 28755
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Выборгское шоссе, 6 Б,лит А",
                "Station_ID": 6,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.5,
                        "AmountOfFuel": 17449
                    },
                    {
                        "Name": "95",
                        "Price": 47.94,
                        "AmountOfFuel": 48202
                    },
                    {
                        "Name": "98",
                        "Price": 54.09,
                        "AmountOfFuel": 21610
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.6,
                        "AmountOfFuel": 17762
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Дальневосточный проспект, 20",
                "Station_ID": 7,
                "data": [
                    {
                        "Name": "92",
                        "Price": 41.5,
                        "AmountOfFuel": 9900
                    },
                    {
                        "Name": "95",
                        "Price": 44.3,
                        "AmountOfFuel": 91094
                    },
                    {
                        "Name": "98",
                        "Price": 54.86,
                        "AmountOfFuel": 98166
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.0,
                        "AmountOfFuel": 11188
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Десантников, 13",
                "Station_ID": 8,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.2,
                        "AmountOfFuel": 76823
                    },
                    {
                        "Name": "95",
                        "Price": 46.7,
                        "AmountOfFuel": 96618
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 61735
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.9,
                        "AmountOfFuel": 14212
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Ириновский проспект, 16",
                "Station_ID": 9,
                "data": [
                    {
                        "Name": "92",
                        "Price": 42.55,
                        "AmountOfFuel": 65759
                    },
                    {
                        "Name": "95",
                        "Price": 45.1,
                        "AmountOfFuel": 14877
                    },
                    {
                        "Name": "98",
                        "Price": 53.17,
                        "AmountOfFuel": 90600
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 50.05,
                        "AmountOfFuel": 27447
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Коллонтай, 8",
                "Station_ID": 10,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.05,
                        "AmountOfFuel": 83814
                    },
                    {
                        "Name": "95",
                        "Price": 46.87,
                        "AmountOfFuel": 54379
                    },
                    {
                        "Name": "98",
                        "Price": 54.28,
                        "AmountOfFuel": 85304
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.39,
                        "AmountOfFuel": 90719
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Коломяжский проспект, 19",
                "Station_ID": 11,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.34,
                        "AmountOfFuel": 71635
                    },
                    {
                        "Name": "95",
                        "Price": 48.94,
                        "AmountOfFuel": 3964
                    },
                    {
                        "Name": "98",
                        "Price": 56.16,
                        "AmountOfFuel": 14830
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.75,
                        "AmountOfFuel": 12456
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Коммуны, 14 литер А",
                "Station_ID": 12,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.35,
                        "AmountOfFuel": 36193
                    },
                    {
                        "Name": "95",
                        "Price": 44.85,
                        "AmountOfFuel": 39307
                    },
                    {
                        "Name": "98",
                        "Price": 54.98,
                        "AmountOfFuel": 95846
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.6,
                        "AmountOfFuel": 69859
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Лапинский проспект, 10",
                "Station_ID": 13,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.07,
                        "AmountOfFuel": 3898
                    },
                    {
                        "Name": "95",
                        "Price": 47.92,
                        "AmountOfFuel": 3637
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 77828
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 51.41,
                        "AmountOfFuel": 70496
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Лахтинский проспект, 2к4",
                "Station_ID": 14,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.8,
                        "AmountOfFuel": 3782
                    },
                    {
                        "Name": "95",
                        "Price": 48.45,
                        "AmountOfFuel": 54395
                    },
                    {
                        "Name": "98",
                        "Price": 54.21,
                        "AmountOfFuel": 21082
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.0,
                        "AmountOfFuel": 96594
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Лахтинский проспект, 114",
                "Station_ID": 15,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.09,
                        "AmountOfFuel": 27700
                    },
                    {
                        "Name": "95",
                        "Price": 48.55,
                        "AmountOfFuel": 93404
                    },
                    {
                        "Name": "98",
                        "Price": 54.22,
                        "AmountOfFuel": 36796
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.76,
                        "AmountOfFuel": 79144
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Ленинский проспект, 61",
                "Station_ID": 16,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.98,
                        "AmountOfFuel": 33954
                    },
                    {
                        "Name": "95",
                        "Price": 48.3,
                        "AmountOfFuel": 30117
                    },
                    {
                        "Name": "98",
                        "Price": 53.51,
                        "AmountOfFuel": 84952
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.39,
                        "AmountOfFuel": 32538
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Малый проспект, 79",
                "Station_ID": 17,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.09,
                        "AmountOfFuel": 60327
                    },
                    {
                        "Name": "95",
                        "Price": 47.67,
                        "AmountOfFuel": 17685
                    },
                    {
                        "Name": "98",
                        "Price": 56.2,
                        "AmountOfFuel": 39562
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.5,
                        "AmountOfFuel": 8925
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Московское шоссе, М10, слева",
                "Station_ID": 18,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.49,
                        "AmountOfFuel": 72769
                    },
                    {
                        "Name": "95",
                        "Price": 47.85,
                        "AmountOfFuel": 63241
                    },
                    {
                        "Name": "98",
                        "Price": 56.09,
                        "AmountOfFuel": 59468
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.69,
                        "AmountOfFuel": 82861
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Московское шоссе, 11, лит.А, М10, справа",
                "Station_ID": 19,
                "data": [
                    {
                        "Name": "92",
                        "Price": 42.4,
                        "AmountOfFuel": 53178
                    },
                    {
                        "Name": "95",
                        "Price": 44.85,
                        "AmountOfFuel": 87751
                    },
                    {
                        "Name": "98",
                        "Price": 51.6,
                        "AmountOfFuel": 86745
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 51.8,
                        "AmountOfFuel": 26554
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Московское шоссе, 50, М10, 687-й км, слева",
                "Station_ID": 20,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.2,
                        "AmountOfFuel": 88314
                    },
                    {
                        "Name": "95",
                        "Price": 46.7,
                        "AmountOfFuel": 45723
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 81765
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.9,
                        "AmountOfFuel": 92130
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Московское шоссе, М10, слева",
                "Station_ID": 21,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.83,
                        "AmountOfFuel": 61919
                    },
                    {
                        "Name": "95",
                        "Price": 47.7,
                        "AmountOfFuel": 50845
                    },
                    {
                        "Name": "98",
                        "Price": 53.15,
                        "AmountOfFuel": 32344
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.4,
                        "AmountOfFuel": 3480
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Московское шоссе, 156 А, М10, слева",
                "Station_ID": 22,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.5,
                        "AmountOfFuel": 16383
                    },
                    {
                        "Name": "95",
                        "Price": 47.94,
                        "AmountOfFuel": 41286
                    },
                    {
                        "Name": "98",
                        "Price": 54.09,
                        "AmountOfFuel": 75068
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.6,
                        "AmountOfFuel": 41868
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Октябрьская набережная, 38, корп.3",
                "Station_ID": 23,
                "data": [
                    {
                        "Name": "92",
                        "Price": 41.5,
                        "AmountOfFuel": 97689
                    },
                    {
                        "Name": "95",
                        "Price": 44.3,
                        "AmountOfFuel": 60473
                    },
                    {
                        "Name": "98",
                        "Price": 54.86,
                        "AmountOfFuel": 11558
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.0,
                        "AmountOfFuel": 4643
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Песочная набережная, 30",
                "Station_ID": 24,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.2,
                        "AmountOfFuel": 17468
                    },
                    {
                        "Name": "95",
                        "Price": 46.7,
                        "AmountOfFuel": 71227
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 50941
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.9,
                        "AmountOfFuel": 28775
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Пискарёвский проспект, 135",
                "Station_ID": 25,
                "data": [
                    {
                        "Name": "92",
                        "Price": 42.55,
                        "AmountOfFuel": 79721
                    },
                    {
                        "Name": "95",
                        "Price": 45.1,
                        "AmountOfFuel": 3666
                    },
                    {
                        "Name": "98",
                        "Price": 53.17,
                        "AmountOfFuel": 52222
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 50.05,
                        "AmountOfFuel": 68280
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Приморское шоссе, 142",
                "Station_ID": 26,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.05,
                        "AmountOfFuel": 90955
                    },
                    {
                        "Name": "95",
                        "Price": 46.87,
                        "AmountOfFuel": 83789
                    },
                    {
                        "Name": "98",
                        "Price": 54.28,
                        "AmountOfFuel": 50723
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.39,
                        "AmountOfFuel": 74784
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Приморское шоссе, 251",
                "Station_ID": 27,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.34,
                        "AmountOfFuel": 26404
                    },
                    {
                        "Name": "95",
                        "Price": 48.94,
                        "AmountOfFuel": 50604
                    },
                    {
                        "Name": "98",
                        "Price": 56.16,
                        "AmountOfFuel": 15978
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.75,
                        "AmountOfFuel": 6626
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, промзона «Парнас», 1-й верхний переулок, 3А",
                "Station_ID": 28,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.35,
                        "AmountOfFuel": 55875
                    },
                    {
                        "Name": "95",
                        "Price": 44.85,
                        "AmountOfFuel": 13526
                    },
                    {
                        "Name": "98",
                        "Price": 54.98,
                        "AmountOfFuel": 39670
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.6,
                        "AmountOfFuel": 24615
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, проспект Маршала Жукова, 23 литер А",
                "Station_ID": 29,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.07,
                        "AmountOfFuel": 73637
                    },
                    {
                        "Name": "95",
                        "Price": 47.92,
                        "AmountOfFuel": 52445
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 17268
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 51.41,
                        "AmountOfFuel": 57977
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, проспект Обуховской обороны, 138",
                "Station_ID": 30,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.8,
                        "AmountOfFuel": 7799
                    },
                    {
                        "Name": "95",
                        "Price": 48.45,
                        "AmountOfFuel": 20706
                    },
                    {
                        "Name": "98",
                        "Price": 54.21,
                        "AmountOfFuel": 94241
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.0,
                        "AmountOfFuel": 68943
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, проспект Энгельса, 179",
                "Station_ID": 31,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.09,
                        "AmountOfFuel": 76260
                    },
                    {
                        "Name": "95",
                        "Price": 48.55,
                        "AmountOfFuel": 5384
                    },
                    {
                        "Name": "98",
                        "Price": 54.22,
                        "AmountOfFuel": 49159
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.76,
                        "AmountOfFuel": 41856
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Пулковское шоссе, 71, Р23, справа",
                "Station_ID": 32,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.98,
                        "AmountOfFuel": 16997
                    },
                    {
                        "Name": "95",
                        "Price": 48.3,
                        "AmountOfFuel": 99594
                    },
                    {
                        "Name": "98",
                        "Price": 53.51,
                        "AmountOfFuel": 32211
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.39,
                        "AmountOfFuel": 85052
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Руставели, 48А",
                "Station_ID": 33,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.09,
                        "AmountOfFuel": 61330
                    },
                    {
                        "Name": "95",
                        "Price": 47.67,
                        "AmountOfFuel": 98916
                    },
                    {
                        "Name": "98",
                        "Price": 56.2,
                        "AmountOfFuel": 43490
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.5,
                        "AmountOfFuel": 51732
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Руставели, 54",
                "Station_ID": 34,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.49,
                        "AmountOfFuel": 55584
                    },
                    {
                        "Name": "95",
                        "Price": 47.85,
                        "AmountOfFuel": 85515
                    },
                    {
                        "Name": "98",
                        "Price": 56.09,
                        "AmountOfFuel": 76949
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.69,
                        "AmountOfFuel": 30617
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Рябовское шоссе, 115 к. 3, лит. А, а/д «Санкт-Петербург - станция Морье» (А128), справа",
                "Station_ID": 35,
                "data": [
                    {
                        "Name": "92",
                        "Price": 42.4,
                        "AmountOfFuel": 70698
                    },
                    {
                        "Name": "95",
                        "Price": 44.85,
                        "AmountOfFuel": 32230
                    },
                    {
                        "Name": "98",
                        "Price": 51.6,
                        "AmountOfFuel": 39864
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 51.8,
                        "AmountOfFuel": 46044
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Салова, 82",
                "Station_ID": 36,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.2,
                        "AmountOfFuel": 87502
                    },
                    {
                        "Name": "95",
                        "Price": 46.7,
                        "AmountOfFuel": 46765
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 49376
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.9,
                        "AmountOfFuel": 77488
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Седова, 1",
                "Station_ID": 37,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.83,
                        "AmountOfFuel": 70034
                    },
                    {
                        "Name": "95",
                        "Price": 47.7,
                        "AmountOfFuel": 33717
                    },
                    {
                        "Name": "98",
                        "Price": 53.15,
                        "AmountOfFuel": 95560
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.4,
                        "AmountOfFuel": 45379
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Софийская",
                "Station_ID": 38,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.5,
                        "AmountOfFuel": 77598
                    },
                    {
                        "Name": "95",
                        "Price": 47.94,
                        "AmountOfFuel": 23323
                    },
                    {
                        "Name": "98",
                        "Price": 54.09,
                        "AmountOfFuel": 38030
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.6,
                        "AmountOfFuel": 54232
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Софийская ул., 17А",
                "Station_ID": 39,
                "data": [
                    {
                        "Name": "92",
                        "Price": 41.5,
                        "AmountOfFuel": 64324
                    },
                    {
                        "Name": "95",
                        "Price": 44.3,
                        "AmountOfFuel": 43383
                    },
                    {
                        "Name": "98",
                        "Price": 54.86,
                        "AmountOfFuel": 11111
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.0,
                        "AmountOfFuel": 88701
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Софийская ул., 60",
                "Station_ID": 40,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.2,
                        "AmountOfFuel": 35792
                    },
                    {
                        "Name": "95",
                        "Price": 46.7,
                        "AmountOfFuel": 45594
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 86159
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 49.9,
                        "AmountOfFuel": 69827
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Софийская ул., 77",
                "Station_ID": 41,
                "data": [
                    {
                        "Name": "92",
                        "Price": 42.55,
                        "AmountOfFuel": 61411
                    },
                    {
                        "Name": "95",
                        "Price": 45.1,
                        "AmountOfFuel": 74703
                    },
                    {
                        "Name": "98",
                        "Price": 53.17,
                        "AmountOfFuel": 23333
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 50.05,
                        "AmountOfFuel": 44951
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Торфяная дорога, 10 литер А",
                "Station_ID": 42,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.05,
                        "AmountOfFuel": 35959
                    },
                    {
                        "Name": "95",
                        "Price": 46.87,
                        "AmountOfFuel": 44347
                    },
                    {
                        "Name": "98",
                        "Price": 54.28,
                        "AmountOfFuel": 22941
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.39,
                        "AmountOfFuel": 98157
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Демьяна Бедного, 15",
                "Station_ID": 43,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.34,
                        "AmountOfFuel": 68985
                    },
                    {
                        "Name": "95",
                        "Price": 48.94,
                        "AmountOfFuel": 81901
                    },
                    {
                        "Name": "98",
                        "Price": 56.16,
                        "AmountOfFuel": 82004
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 47.75,
                        "AmountOfFuel": 39685
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Планерная, 22",
                "Station_ID": 44,
                "data": [
                    {
                        "Name": "92",
                        "Price": 43.35,
                        "AmountOfFuel": 62310
                    },
                    {
                        "Name": "95",
                        "Price": 44.85,
                        "AmountOfFuel": 75340
                    },
                    {
                        "Name": "98",
                        "Price": 54.98,
                        "AmountOfFuel": 98162
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.6,
                        "AmountOfFuel": 15447
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, ул. Студенческая, 15",
                "Station_ID": 45,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.07,
                        "AmountOfFuel": 36741
                    },
                    {
                        "Name": "95",
                        "Price": 47.92,
                        "AmountOfFuel": 95742
                    },
                    {
                        "Name": "98",
                        "Price": 54.61,
                        "AmountOfFuel": 41024
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 51.41,
                        "AmountOfFuel": 94751
                    }
                ]
            },
            {
                "Address": "г. Санкт-Петербург, Шафировский проспект, 24А",
                "Station_ID": 46,
                "data": [
                    {
                        "Name": "92",
                        "Price": 44.8,
                        "AmountOfFuel": 93686
                    },
                    {
                        "Name": "95",
                        "Price": 48.45,
                        "AmountOfFuel": 75305
                    },
                    {
                        "Name": "98",
                        "Price": 54.21,
                        "AmountOfFuel": 18799
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.0,
                        "AmountOfFuel": 18829
                    }
                ]
            },
            {
                "Address": "пос. Шушары, Пулковское шоссе, д. 110, лит. А, Р23, слева",
                "Station_ID": 47,
                "data": [
                    {
                        "Name": "92",
                        "Price": 45.09,
                        "AmountOfFuel": 93265
                    },
                    {
                        "Name": "95",
                        "Price": 48.55,
                        "AmountOfFuel": 5457
                    },
                    {
                        "Name": "98",
                        "Price": 54.22,
                        "AmountOfFuel": 83114
                    },
                    {
                        "Name": "Disel Fuel",
                        "Price": 48.76,
                        "AmountOfFuel": 44985
                    }
                ]
            }
        ]

        with transaction.atomic():
            for station_data in json_data:
                station = FuelStation.objects.create(
                    Station_ID=station_data["Station_ID"],
                    Address=station_data["Address"],
                )

                for fuel_data in station_data["data"]:
                    fuel, created = Fuel.objects.get_or_create(Name=fuel_data["Name"])

                    FuelPrices.objects.create(
                        Station_ID=station,
                        Fuel_ID=fuel,
                        Price=fuel_data["Price"],
                        AmountOfFuel=fuel_data["AmountOfFuel"],
                    )

        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
