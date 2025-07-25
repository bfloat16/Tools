# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class OperatorExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OperatorExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOperatorExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # OperatorExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OperatorExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OperatorExcel
    def OperatorCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def OutputSequence(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def RandomWeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def OutputDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def OperatorOutputPriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OperatorExcel
    def PortraitPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OperatorExcel
    def TextLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OperatorExcel
    def VoiceId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # OperatorExcel
    def VoiceIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # OperatorExcel
    def VoiceIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OperatorExcel
    def VoiceIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # OperatorExcel
    def OperatorWaitQueue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def OperatorExcelStart(builder):
    builder.StartObject(12)

def Start(builder):
    OperatorExcelStart(builder)

def OperatorExcelAddUniqueId(builder, uniqueId):
    builder.PrependInt64Slot(0, uniqueId, 0)

def AddUniqueId(builder, uniqueId):
    OperatorExcelAddUniqueId(builder, uniqueId)

def OperatorExcelAddGroupId(builder, groupId):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(groupId), 0)

def AddGroupId(builder, groupId):
    OperatorExcelAddGroupId(builder, groupId)

def OperatorExcelAddOperatorCondition(builder, operatorCondition):
    builder.PrependInt32Slot(2, operatorCondition, 0)

def AddOperatorCondition(builder, operatorCondition):
    OperatorExcelAddOperatorCondition(builder, operatorCondition)

def OperatorExcelAddOutputSequence(builder, outputSequence):
    builder.PrependInt32Slot(3, outputSequence, 0)

def AddOutputSequence(builder, outputSequence):
    OperatorExcelAddOutputSequence(builder, outputSequence)

def OperatorExcelAddRandomWeight(builder, randomWeight):
    builder.PrependInt32Slot(4, randomWeight, 0)

def AddRandomWeight(builder, randomWeight):
    OperatorExcelAddRandomWeight(builder, randomWeight)

def OperatorExcelAddOutputDelay(builder, outputDelay):
    builder.PrependInt32Slot(5, outputDelay, 0)

def AddOutputDelay(builder, outputDelay):
    OperatorExcelAddOutputDelay(builder, outputDelay)

def OperatorExcelAddDuration(builder, duration):
    builder.PrependInt32Slot(6, duration, 0)

def AddDuration(builder, duration):
    OperatorExcelAddDuration(builder, duration)

def OperatorExcelAddOperatorOutputPriority(builder, operatorOutputPriority):
    builder.PrependInt32Slot(7, operatorOutputPriority, 0)

def AddOperatorOutputPriority(builder, operatorOutputPriority):
    OperatorExcelAddOperatorOutputPriority(builder, operatorOutputPriority)

def OperatorExcelAddPortraitPath(builder, portraitPath):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(portraitPath), 0)

def AddPortraitPath(builder, portraitPath):
    OperatorExcelAddPortraitPath(builder, portraitPath)

def OperatorExcelAddTextLocalizeKey(builder, textLocalizeKey):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(textLocalizeKey), 0)

def AddTextLocalizeKey(builder, textLocalizeKey):
    OperatorExcelAddTextLocalizeKey(builder, textLocalizeKey)

def OperatorExcelAddVoiceId(builder, voiceId):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(voiceId), 0)

def AddVoiceId(builder, voiceId):
    OperatorExcelAddVoiceId(builder, voiceId)

def OperatorExcelStartVoiceIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartVoiceIdVector(builder, numElems):
    return OperatorExcelStartVoiceIdVector(builder, numElems)

def OperatorExcelAddOperatorWaitQueue(builder, operatorWaitQueue):
    builder.PrependBoolSlot(11, operatorWaitQueue, 0)

def AddOperatorWaitQueue(builder, operatorWaitQueue):
    OperatorExcelAddOperatorWaitQueue(builder, operatorWaitQueue)

def OperatorExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return OperatorExcelEnd(builder)
