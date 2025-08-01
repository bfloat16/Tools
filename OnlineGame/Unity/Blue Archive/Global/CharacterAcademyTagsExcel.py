# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterAcademyTagsExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterAcademyTagsExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterAcademyTagsExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterAcademyTagsExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterAcademyTagsExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterAcademyTagsExcel
    def FavorTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def FavorTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # CharacterAcademyTagsExcel
    def FavorItemTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # CharacterAcademyTagsExcel
    def FavorItemUniqueTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemUniqueTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemUniqueTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def FavorItemUniqueTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # CharacterAcademyTagsExcel
    def ForbiddenTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def ForbiddenTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def ForbiddenTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def ForbiddenTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # CharacterAcademyTagsExcel
    def ZoneWhiteListTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterAcademyTagsExcel
    def ZoneWhiteListTagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterAcademyTagsExcel
    def ZoneWhiteListTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterAcademyTagsExcel
    def ZoneWhiteListTagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def CharacterAcademyTagsExcelStart(builder):
    builder.StartObject(6)

def Start(builder):
    CharacterAcademyTagsExcelStart(builder)

def CharacterAcademyTagsExcelAddId(builder, id):
    builder.PrependInt64Slot(0, id, 0)

def AddId(builder, id):
    CharacterAcademyTagsExcelAddId(builder, id)

def CharacterAcademyTagsExcelAddFavorTags(builder, favorTags):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(favorTags), 0)

def AddFavorTags(builder, favorTags):
    CharacterAcademyTagsExcelAddFavorTags(builder, favorTags)

def CharacterAcademyTagsExcelStartFavorTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartFavorTagsVector(builder, numElems):
    return CharacterAcademyTagsExcelStartFavorTagsVector(builder, numElems)

def CharacterAcademyTagsExcelAddFavorItemTags(builder, favorItemTags):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(favorItemTags), 0)

def AddFavorItemTags(builder, favorItemTags):
    CharacterAcademyTagsExcelAddFavorItemTags(builder, favorItemTags)

def CharacterAcademyTagsExcelStartFavorItemTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartFavorItemTagsVector(builder, numElems):
    return CharacterAcademyTagsExcelStartFavorItemTagsVector(builder, numElems)

def CharacterAcademyTagsExcelAddFavorItemUniqueTags(builder, favorItemUniqueTags):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(favorItemUniqueTags), 0)

def AddFavorItemUniqueTags(builder, favorItemUniqueTags):
    CharacterAcademyTagsExcelAddFavorItemUniqueTags(builder, favorItemUniqueTags)

def CharacterAcademyTagsExcelStartFavorItemUniqueTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartFavorItemUniqueTagsVector(builder, numElems):
    return CharacterAcademyTagsExcelStartFavorItemUniqueTagsVector(builder, numElems)

def CharacterAcademyTagsExcelAddForbiddenTags(builder, forbiddenTags):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(forbiddenTags), 0)

def AddForbiddenTags(builder, forbiddenTags):
    CharacterAcademyTagsExcelAddForbiddenTags(builder, forbiddenTags)

def CharacterAcademyTagsExcelStartForbiddenTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartForbiddenTagsVector(builder, numElems):
    return CharacterAcademyTagsExcelStartForbiddenTagsVector(builder, numElems)

def CharacterAcademyTagsExcelAddZoneWhiteListTags(builder, zoneWhiteListTags):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(zoneWhiteListTags), 0)

def AddZoneWhiteListTags(builder, zoneWhiteListTags):
    CharacterAcademyTagsExcelAddZoneWhiteListTags(builder, zoneWhiteListTags)

def CharacterAcademyTagsExcelStartZoneWhiteListTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartZoneWhiteListTagsVector(builder, numElems):
    return CharacterAcademyTagsExcelStartZoneWhiteListTagsVector(builder, numElems)

def CharacterAcademyTagsExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return CharacterAcademyTagsExcelEnd(builder)
