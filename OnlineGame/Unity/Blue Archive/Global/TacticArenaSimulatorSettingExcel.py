# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticArenaSimulatorSettingExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticArenaSimulatorSettingExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTacticArenaSimulatorSettingExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TacticArenaSimulatorSettingExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TacticArenaSimulatorSettingExcel
    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def Repeat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerUserArenaGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerUserArenaRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerPresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerStrikerNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def AttackerSpecialNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderUserArenaGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderUserArenaRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderPresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderStrikerNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def DefenderSpecialNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticArenaSimulatorSettingExcel
    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def TacticArenaSimulatorSettingExcelStart(builder):
    builder.StartObject(15)

def Start(builder):
    TacticArenaSimulatorSettingExcelStart(builder)

def TacticArenaSimulatorSettingExcelAddOrder(builder, order):
    builder.PrependInt64Slot(0, order, 0)

def AddOrder(builder, order):
    TacticArenaSimulatorSettingExcelAddOrder(builder, order)

def TacticArenaSimulatorSettingExcelAddRepeat(builder, repeat):
    builder.PrependInt64Slot(1, repeat, 0)

def AddRepeat(builder, repeat):
    TacticArenaSimulatorSettingExcelAddRepeat(builder, repeat)

def TacticArenaSimulatorSettingExcelAddAttackerFrom(builder, attackerFrom):
    builder.PrependInt32Slot(2, attackerFrom, 0)

def AddAttackerFrom(builder, attackerFrom):
    TacticArenaSimulatorSettingExcelAddAttackerFrom(builder, attackerFrom)

def TacticArenaSimulatorSettingExcelAddAttackerUserArenaGroup(builder, attackerUserArenaGroup):
    builder.PrependInt64Slot(3, attackerUserArenaGroup, 0)

def AddAttackerUserArenaGroup(builder, attackerUserArenaGroup):
    TacticArenaSimulatorSettingExcelAddAttackerUserArenaGroup(builder, attackerUserArenaGroup)

def TacticArenaSimulatorSettingExcelAddAttackerUserArenaRank(builder, attackerUserArenaRank):
    builder.PrependInt64Slot(4, attackerUserArenaRank, 0)

def AddAttackerUserArenaRank(builder, attackerUserArenaRank):
    TacticArenaSimulatorSettingExcelAddAttackerUserArenaRank(builder, attackerUserArenaRank)

def TacticArenaSimulatorSettingExcelAddAttackerPresetGroupId(builder, attackerPresetGroupId):
    builder.PrependInt64Slot(5, attackerPresetGroupId, 0)

def AddAttackerPresetGroupId(builder, attackerPresetGroupId):
    TacticArenaSimulatorSettingExcelAddAttackerPresetGroupId(builder, attackerPresetGroupId)

def TacticArenaSimulatorSettingExcelAddAttackerStrikerNum(builder, attackerStrikerNum):
    builder.PrependInt64Slot(6, attackerStrikerNum, 0)

def AddAttackerStrikerNum(builder, attackerStrikerNum):
    TacticArenaSimulatorSettingExcelAddAttackerStrikerNum(builder, attackerStrikerNum)

def TacticArenaSimulatorSettingExcelAddAttackerSpecialNum(builder, attackerSpecialNum):
    builder.PrependInt64Slot(7, attackerSpecialNum, 0)

def AddAttackerSpecialNum(builder, attackerSpecialNum):
    TacticArenaSimulatorSettingExcelAddAttackerSpecialNum(builder, attackerSpecialNum)

def TacticArenaSimulatorSettingExcelAddDefenderFrom(builder, defenderFrom):
    builder.PrependInt32Slot(8, defenderFrom, 0)

def AddDefenderFrom(builder, defenderFrom):
    TacticArenaSimulatorSettingExcelAddDefenderFrom(builder, defenderFrom)

def TacticArenaSimulatorSettingExcelAddDefenderUserArenaGroup(builder, defenderUserArenaGroup):
    builder.PrependInt64Slot(9, defenderUserArenaGroup, 0)

def AddDefenderUserArenaGroup(builder, defenderUserArenaGroup):
    TacticArenaSimulatorSettingExcelAddDefenderUserArenaGroup(builder, defenderUserArenaGroup)

def TacticArenaSimulatorSettingExcelAddDefenderUserArenaRank(builder, defenderUserArenaRank):
    builder.PrependInt64Slot(10, defenderUserArenaRank, 0)

def AddDefenderUserArenaRank(builder, defenderUserArenaRank):
    TacticArenaSimulatorSettingExcelAddDefenderUserArenaRank(builder, defenderUserArenaRank)

def TacticArenaSimulatorSettingExcelAddDefenderPresetGroupId(builder, defenderPresetGroupId):
    builder.PrependInt64Slot(11, defenderPresetGroupId, 0)

def AddDefenderPresetGroupId(builder, defenderPresetGroupId):
    TacticArenaSimulatorSettingExcelAddDefenderPresetGroupId(builder, defenderPresetGroupId)

def TacticArenaSimulatorSettingExcelAddDefenderStrikerNum(builder, defenderStrikerNum):
    builder.PrependInt64Slot(12, defenderStrikerNum, 0)

def AddDefenderStrikerNum(builder, defenderStrikerNum):
    TacticArenaSimulatorSettingExcelAddDefenderStrikerNum(builder, defenderStrikerNum)

def TacticArenaSimulatorSettingExcelAddDefenderSpecialNum(builder, defenderSpecialNum):
    builder.PrependInt64Slot(13, defenderSpecialNum, 0)

def AddDefenderSpecialNum(builder, defenderSpecialNum):
    TacticArenaSimulatorSettingExcelAddDefenderSpecialNum(builder, defenderSpecialNum)

def TacticArenaSimulatorSettingExcelAddGroundId(builder, groundId):
    builder.PrependInt64Slot(14, groundId, 0)

def AddGroundId(builder, groundId):
    TacticArenaSimulatorSettingExcelAddGroundId(builder, groundId)

def TacticArenaSimulatorSettingExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return TacticArenaSimulatorSettingExcelEnd(builder)
