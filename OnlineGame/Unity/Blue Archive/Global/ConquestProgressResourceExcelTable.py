# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestProgressResourceExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestProgressResourceExcelTable()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConquestProgressResourceExcelTable(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConquestProgressResourceExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestProgressResourceExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Global.ConquestProgressResourceExcel import ConquestProgressResourceExcel
            obj = ConquestProgressResourceExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ConquestProgressResourceExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConquestProgressResourceExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def ConquestProgressResourceExcelTableStart(builder):
    builder.StartObject(1)

def Start(builder):
    ConquestProgressResourceExcelTableStart(builder)

def ConquestProgressResourceExcelTableAddDataList(builder, dataList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(dataList), 0)

def AddDataList(builder, dataList):
    ConquestProgressResourceExcelTableAddDataList(builder, dataList)

def ConquestProgressResourceExcelTableStartDataListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDataListVector(builder, numElems):
    return ConquestProgressResourceExcelTableStartDataListVector(builder, numElems)

def ConquestProgressResourceExcelTableEnd(builder):
    return builder.EndObject()

def End(builder):
    return ConquestProgressResourceExcelTableEnd(builder)
