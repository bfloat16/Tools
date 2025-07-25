# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FarmingDungeonLocationManageExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FarmingDungeonLocationManageExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFarmingDungeonLocationManageExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FarmingDungeonLocationManageExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FarmingDungeonLocationManageExcel
    def FarmingDungeonLocationId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FarmingDungeonLocationManageExcel
    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FarmingDungeonLocationManageExcel
    def WeekDungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FarmingDungeonLocationManageExcel
    def SchoolDungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FarmingDungeonLocationManageExcel
    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FarmingDungeonLocationManageExcel
    def OpenStartDateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FarmingDungeonLocationManageExcel
    def OpenEndDateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FarmingDungeonLocationManageExcel
    def LocationButtonImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FarmingDungeonLocationManageExcel
    def LocalizeCodeTitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # FarmingDungeonLocationManageExcel
    def LocalizeCodeInfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def FarmingDungeonLocationManageExcelStart(builder):
    builder.StartObject(10)

def Start(builder):
    FarmingDungeonLocationManageExcelStart(builder)

def FarmingDungeonLocationManageExcelAddFarmingDungeonLocationId(builder, farmingDungeonLocationId):
    builder.PrependInt64Slot(0, farmingDungeonLocationId, 0)

def AddFarmingDungeonLocationId(builder, farmingDungeonLocationId):
    FarmingDungeonLocationManageExcelAddFarmingDungeonLocationId(builder, farmingDungeonLocationId)

def FarmingDungeonLocationManageExcelAddContentType(builder, contentType):
    builder.PrependInt32Slot(1, contentType, 0)

def AddContentType(builder, contentType):
    FarmingDungeonLocationManageExcelAddContentType(builder, contentType)

def FarmingDungeonLocationManageExcelAddWeekDungeonType(builder, weekDungeonType):
    builder.PrependInt32Slot(2, weekDungeonType, 0)

def AddWeekDungeonType(builder, weekDungeonType):
    FarmingDungeonLocationManageExcelAddWeekDungeonType(builder, weekDungeonType)

def FarmingDungeonLocationManageExcelAddSchoolDungeonType(builder, schoolDungeonType):
    builder.PrependInt32Slot(3, schoolDungeonType, 0)

def AddSchoolDungeonType(builder, schoolDungeonType):
    FarmingDungeonLocationManageExcelAddSchoolDungeonType(builder, schoolDungeonType)

def FarmingDungeonLocationManageExcelAddOrder(builder, order):
    builder.PrependInt64Slot(4, order, 0)

def AddOrder(builder, order):
    FarmingDungeonLocationManageExcelAddOrder(builder, order)

def FarmingDungeonLocationManageExcelAddOpenStartDateTime(builder, openStartDateTime):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(openStartDateTime), 0)

def AddOpenStartDateTime(builder, openStartDateTime):
    FarmingDungeonLocationManageExcelAddOpenStartDateTime(builder, openStartDateTime)

def FarmingDungeonLocationManageExcelAddOpenEndDateTime(builder, openEndDateTime):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(openEndDateTime), 0)

def AddOpenEndDateTime(builder, openEndDateTime):
    FarmingDungeonLocationManageExcelAddOpenEndDateTime(builder, openEndDateTime)

def FarmingDungeonLocationManageExcelAddLocationButtonImagePath(builder, locationButtonImagePath):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(locationButtonImagePath), 0)

def AddLocationButtonImagePath(builder, locationButtonImagePath):
    FarmingDungeonLocationManageExcelAddLocationButtonImagePath(builder, locationButtonImagePath)

def FarmingDungeonLocationManageExcelAddLocalizeCodeTitle(builder, localizeCodeTitle):
    builder.PrependUint32Slot(8, localizeCodeTitle, 0)

def AddLocalizeCodeTitle(builder, localizeCodeTitle):
    FarmingDungeonLocationManageExcelAddLocalizeCodeTitle(builder, localizeCodeTitle)

def FarmingDungeonLocationManageExcelAddLocalizeCodeInfo(builder, localizeCodeInfo):
    builder.PrependUint32Slot(9, localizeCodeInfo, 0)

def AddLocalizeCodeInfo(builder, localizeCodeInfo):
    FarmingDungeonLocationManageExcelAddLocalizeCodeInfo(builder, localizeCodeInfo)

def FarmingDungeonLocationManageExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return FarmingDungeonLocationManageExcelEnd(builder)
