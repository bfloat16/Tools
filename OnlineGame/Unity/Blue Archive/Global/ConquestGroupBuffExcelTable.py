# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestGroupBuffExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestGroupBuffExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConquestGroupBuffExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConquestGroupBuffExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestGroupBuffExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.ConquestGroupBuffExcel import ConquestGroupBuffExcel
            obj = ConquestGroupBuffExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ConquestGroupBuffExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestGroupBuffExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def ConquestGroupBuffExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    ConquestGroupBuffExcelTableStart(builder)

def ConquestGroupBuffExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    ConquestGroupBuffExcelTableAddDataList(builder, dataList)

def ConquestGroupBuffExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return ConquestGroupBuffExcelTableStartDataListVector(builder, numElems)

def ConquestGroupBuffExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return ConquestGroupBuffExcelTableEnd(builder)
