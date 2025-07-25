# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EmoticonSpecialExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EmoticonSpecialExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEmoticonSpecialExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EmoticonSpecialExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EmoticonSpecialExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EmoticonSpecialExcel
    def CharacterUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EmoticonSpecialExcel
    def Random(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def EmoticonSpecialExcelStart(builder):
    builder.StartObject(3)

def Start(builder):
    EmoticonSpecialExcelStart(builder)

def EmoticonSpecialExcelAddUniqueId(builder, uniqueId):
    builder.PrependInt64Slot(0, uniqueId, 0)

def AddUniqueId(builder, uniqueId):
    EmoticonSpecialExcelAddUniqueId(builder, uniqueId)

def EmoticonSpecialExcelAddCharacterUniqueId(builder, characterUniqueId):
    builder.PrependInt64Slot(1, characterUniqueId, 0)

def AddCharacterUniqueId(builder, characterUniqueId):
    EmoticonSpecialExcelAddCharacterUniqueId(builder, characterUniqueId)

def EmoticonSpecialExcelAddRandom(builder, random):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(random), 0)

def AddRandom(builder, random):
    EmoticonSpecialExcelAddRandom(builder, random)

def EmoticonSpecialExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return EmoticonSpecialExcelEnd(builder)
