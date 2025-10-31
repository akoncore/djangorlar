# orm_like_examples.py
# Пример, похожий на ORM: простая реализация хранения данных в памяти.
# Поддерживает .save() и .filter() как в Django ORM.

class InMemoryDB:
    def __init__(self):
        self._tables = {}

    def table(self, name):
        """Возвращает таблицу (список объектов) по имени модели."""
        if name not in self._tables:
            self._tables[name] = []
        return self._tables[name]

db = InMemoryDB()

class Field:
    """Определяет поле модели (с дефолтным значением)."""
    def __init__(self, default=None):
        self.default = default

class ModelMeta(type):
    """Метакласс, собирающий все поля модели."""
    def __new__(cls, name, bases, attrs):
        fields = {k: a for k, a in attrs.items() if isinstance(a, Field)}
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    """Базовый класс для всех моделей."""
    def __init__(self, **kwargs):
        for fname, field in self._fields.items():
            setattr(self, fname, kwargs.get(fname, field.default))
        self.id = None

    @classmethod
    def objects(cls):
        """Возвращает QuerySet для модели."""
        return QuerySet(cls)

    def save(self):
        """Сохраняет объект в базе (создание или обновление)."""
        table = db.table(self.__class__.__name__)
        if self.id is None:
            self.id = len(table) + 1
            table.append(self)
        else:
            for i, obj in enumerate(table):
                if obj.id == self.id:
                    table[i] = self
                    break

class QuerySet:
    """Позволяет фильтровать и получать данные из таблицы."""
    def __init__(self, model):
        self.model = model
        self._filters = []

    def filter(self, **kwargs):
        """Добавляет фильтр."""
        q = QuerySet(self.model)
        q._filters = self._filters + [kwargs]
        return q

    def all(self):
        """Возвращает все объекты, соответствующие фильтрам."""
        table = db.table(self.model.__name__)
        results = table[:]
        for cond in self._filters:
            results = [obj for obj in results if all(getattr(obj, k) == v for k, v in cond.items())]
        return results

# Пример модели
class Person(Model):
    name = Field(default='')
    age = Field(default=0)
    male = bool(True)
class Comment(Model):
    title = Field(default='')
    content = Field(default="None")
    name = Person()
    
if __name__ == '__main__':
    p1 = Person(name='AKon', age=22,male = True); p1.save()
    p2 = Person(name='Sam', age=26); p2.save()
    p3 = Person(name='Akon', age=30); p3.save()
    c1 = Comment(title='DDD', content='aa',name = p1.name); c1.save()

    print('Все люди:', [(p.id, p.name, p.age) for p in Person.objects().all()])
    print('Фильтр name=Ainur:', [(p.id, p.name, p.age) for p in Person.objects().filter(name='Akon').all()])

    p1.age = 23 ,p1.save()
    print(p1.age)
    
    print(c1)