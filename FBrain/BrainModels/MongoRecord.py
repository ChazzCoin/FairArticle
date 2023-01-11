from F import DICT, DATE
from F.CLASS import FairClass
from F.TYPE.Dict import FairDict

""" Smart dict:type wrapper for Single MongoDB Record."""
class Record(FairDict):
    _id = ""
    fields = []
    original_record = None

    def __init__(self, record, **kwargs):
        super().__init__(**kwargs)
        self.original_record = record
        self.import_record(record)

    def import_record(self, record:dict):
        if not record:
            return None
        self._id = DICT.get("_id", record, "Unknown")
        self._add_fields(record)
        self.update(record)

    def _add_fields(self, record:dict):
        for key in record.keys():
            self.fields.append(key)

    def get_field(self, fieldName):
        return self[fieldName]

    def get_embeddedDict(self, fieldName, key):
        obj: dict = self.get_field(fieldName)
        embedded_obj = DICT.get(key, obj, None)
        return embedded_obj

    def update_updatedDate(self):
        self["updatedDate"] = DATE.TODAY

    def update_field(self, fieldName, value):
        self[fieldName] = value
        self.update_updatedDate()

    def export(self, isUpdate=False):
        if isUpdate:
            self.update_updatedDate()
        result = {}
        for f in self.fields:
            result[f] = self[f]
        return result



""" Smart list:type wrapper for List of MongoDB Records."""
class Records(list, FairClass):
    collection_name = ""

    def import_records(self, records:list):
        for rec in records:
            newR = Record(rec)
            self.append(newR)

    def loop_exported(self) -> dict:
        for rec in self:
            rec: Record
            yield rec.export()

    def loop_records(self) -> Record:
        for rec in self:
            rec: Record
            yield rec




# class SmartRecords(Record):
#     mapped_fields = {}
#
#     def map_field(self, key, field):
#         self.mapped_fields[key] = field
#
#     # def import_mongo_records(self, records):
#     #     for item in records:
#     #         item: dict
#     #         keyList = item.keys()
#     #         for key in item:
#     #             self.mapped_fields[]
#
#     def test(self):
#         for f in self.fields:
#             mapped = {keyField: keyList, valueField: valueList}
#
#     def map_dict(self, keyField: str, valueField: str, sortByKey=True):
#         dic = self
#         if sortByKey:
#             dic = self.SORT_BY_KEY(super(), False)
#         keyList = self.converter.dict_TO_List_OF_Keys(dic)
#         valueList = self.converter.dict_TO_List_OF_Values(dic)
#         mapped = { keyField: keyList, valueField: valueList }
#         return mapped


"""
db = "research"
collection = "articles

fields = [ "_id", "title", "date" ]
single_article = {"_id": "1234", "title": "hey there", "date": "july 24 2022"}



"""
# example = [{"_id": "1234", "title": "hey there", "date": "july 24 2022"},
#            {"_id": "4321", "title": "something cool", "date": "august 02 2020"}]
#
# result = { "july 24 2022": {"_id": "1234", "title": "hey there", "date": "july 24 2022"},
#            "august 02 2020": {"_id": "4321", "title": "something cool", "date": "august 02 2020"} }


# t = SmartRecord()
# print(t.set_collection_name("fake_articles"))
#
# t["test"] = "poop"
# t["test2"] = "poop2"
# # print(t["test2"])
# print(t.safe_get("test", default="Justice"))
# print(t["test2"])