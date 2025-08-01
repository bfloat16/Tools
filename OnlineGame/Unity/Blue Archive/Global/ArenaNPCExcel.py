# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ArenaNPCExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArenaNPCExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsArenaNPCExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ArenaNPCExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArenaNPCExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaNPCExcel
    def Rank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaNPCExcel
    def NpcaccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaNPCExcel
    def Npclevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaNPCExcel
    def NpclevelDeviation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaNPCExcel
    def NpcstarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ArenaNPCExcel
    def ExceptionCharacterRarities(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ArenaNPCExcel
    def ExceptionCharacterRaritiesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ArenaNPCExcel
    def ExceptionCharacterRaritiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaNPCExcel
    def ExceptionCharacterRaritiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # ArenaNPCExcel
    def ExceptionMainCharacterIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaNPCExcel
    def ExceptionMainCharacterIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaNPCExcel
    def ExceptionMainCharacterIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaNPCExcel
    def ExceptionMainCharacterIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # ArenaNPCExcel
    def ExceptionSupportCharacterIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaNPCExcel
    def ExceptionSupportCharacterIdsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaNPCExcel
    def ExceptionSupportCharacterIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaNPCExcel
    def ExceptionSupportCharacterIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # ArenaNPCExcel
    def ExceptionTssids(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArenaNPCExcel
    def ExceptionTssidsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ArenaNPCExcel
    def ExceptionTssidsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ArenaNPCExcel
    def ExceptionTssidsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

def ArenaNPCExcelStart(builder):
    builder.StartObject(10)

def Start(builder):
    ArenaNPCExcelStart(builder)

def ArenaNPCExcelAddUniqueId(builder, uniqueId):
    builder.PrependInt64Slot(0, uniqueId, 0)

def AddUniqueId(builder, uniqueId):
    ArenaNPCExcelAddUniqueId(builder, uniqueId)

def ArenaNPCExcelAddRank(builder, rank):
    builder.PrependInt64Slot(1, rank, 0)

def AddRank(builder, rank):
    ArenaNPCExcelAddRank(builder, rank)

def ArenaNPCExcelAddNpcaccountLevel(builder, npcaccountLevel):
    builder.PrependInt64Slot(2, npcaccountLevel, 0)

def AddNpcaccountLevel(builder, npcaccountLevel):
    ArenaNPCExcelAddNpcaccountLevel(builder, npcaccountLevel)

def ArenaNPCExcelAddNpclevel(builder, npclevel):
    builder.PrependInt64Slot(3, npclevel, 0)

def AddNpclevel(builder, npclevel):
    ArenaNPCExcelAddNpclevel(builder, npclevel)

def ArenaNPCExcelAddNpclevelDeviation(builder, npclevelDeviation):
    builder.PrependInt64Slot(4, npclevelDeviation, 0)

def AddNpclevelDeviation(builder, npclevelDeviation):
    ArenaNPCExcelAddNpclevelDeviation(builder, npclevelDeviation)

def ArenaNPCExcelAddNpcstarGrade(builder, npcstarGrade):
    builder.PrependInt64Slot(5, npcstarGrade, 0)

def AddNpcstarGrade(builder, npcstarGrade):
    ArenaNPCExcelAddNpcstarGrade(builder, npcstarGrade)

def ArenaNPCExcelAddExceptionCharacterRarities(builder, exceptionCharacterRarities):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(exceptionCharacterRarities), 0)

def AddExceptionCharacterRarities(builder, exceptionCharacterRarities):
    ArenaNPCExcelAddExceptionCharacterRarities(builder, exceptionCharacterRarities)

def ArenaNPCExcelStartExceptionCharacterRaritiesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartExceptionCharacterRaritiesVector(builder, numElems):
    return ArenaNPCExcelStartExceptionCharacterRaritiesVector(builder, numElems)

def ArenaNPCExcelAddExceptionMainCharacterIds(builder, exceptionMainCharacterIds):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(exceptionMainCharacterIds), 0)

def AddExceptionMainCharacterIds(builder, exceptionMainCharacterIds):
    ArenaNPCExcelAddExceptionMainCharacterIds(builder, exceptionMainCharacterIds)

def ArenaNPCExcelStartExceptionMainCharacterIdsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartExceptionMainCharacterIdsVector(builder, numElems):
    return ArenaNPCExcelStartExceptionMainCharacterIdsVector(builder, numElems)

def ArenaNPCExcelAddExceptionSupportCharacterIds(builder, exceptionSupportCharacterIds):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(exceptionSupportCharacterIds), 0)

def AddExceptionSupportCharacterIds(builder, exceptionSupportCharacterIds):
    ArenaNPCExcelAddExceptionSupportCharacterIds(builder, exceptionSupportCharacterIds)

def ArenaNPCExcelStartExceptionSupportCharacterIdsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartExceptionSupportCharacterIdsVector(builder, numElems):
    return ArenaNPCExcelStartExceptionSupportCharacterIdsVector(builder, numElems)

def ArenaNPCExcelAddExceptionTssids(builder, exceptionTssids):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(exceptionTssids), 0)

def AddExceptionTssids(builder, exceptionTssids):
    ArenaNPCExcelAddExceptionTssids(builder, exceptionTssids)

def ArenaNPCExcelStartExceptionTssidsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)

def StartExceptionTssidsVector(builder, numElems):
    return ArenaNPCExcelStartExceptionTssidsVector(builder, numElems)

def ArenaNPCExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return ArenaNPCExcelEnd(builder)
