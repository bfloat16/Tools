# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidStageExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidStageExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEliminateRaidStageExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EliminateRaidStageExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EliminateRaidStageExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.EliminateRaidStageExcel import EliminateRaidStageExcel
            obj = EliminateRaidStageExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # EliminateRaidStageExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EliminateRaidStageExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def EliminateRaidStageExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    EliminateRaidStageExcelTableStart(builder)

def EliminateRaidStageExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    EliminateRaidStageExcelTableAddDataList(builder, dataList)

def EliminateRaidStageExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return EliminateRaidStageExcelTableStartDataListVector(builder, numElems)

def EliminateRaidStageExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return EliminateRaidStageExcelTableEnd(builder)
