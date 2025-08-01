# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PersonalityExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PersonalityExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPersonalityExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # PersonalityExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PersonalityExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PersonalityExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def PersonalityExcelStart(builder):
    builder.StartObject(2)

def Start(builder):
    PersonalityExcelStart(builder)

def PersonalityExcelAddId(builder, id):
    builder.PrependInt64Slot(0, id, 0)

def AddId(builder, id):
    PersonalityExcelAddId(builder, id)

def PersonalityExcelAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    PersonalityExcelAddName(builder, name)

def PersonalityExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return PersonalityExcelEnd(builder)
