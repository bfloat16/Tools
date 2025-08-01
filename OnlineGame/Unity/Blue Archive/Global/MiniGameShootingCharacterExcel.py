# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameShootingCharacterExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameShootingCharacterExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameShootingCharacterExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameShootingCharacterExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameShootingCharacterExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def SpineResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def BodyRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MiniGameShootingCharacterExcel
    def ModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def NormalAttackSkillData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def PublicSkillData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # MiniGameShootingCharacterExcel
    def PublicSkillDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameShootingCharacterExcel
    def PublicSkillDataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # MiniGameShootingCharacterExcel
    def DeathSkillData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameShootingCharacterExcel
    def MaxHp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def AttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def DefensePower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def CriticalRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def CriticalDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def AttackRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def MoveSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def ShotTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameShootingCharacterExcel
    def IsBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameShootingCharacterExcel
    def Scale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MiniGameShootingCharacterExcel
    def IgnoreObstacleCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameShootingCharacterExcel
    def CharacterVoiceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def MiniGameShootingCharacterExcelStart(builder):
    builder.StartObject(19)

def Start(builder):
    MiniGameShootingCharacterExcelStart(builder)

def MiniGameShootingCharacterExcelAddUniqueId(builder, uniqueId):
    builder.PrependInt64Slot(0, uniqueId, 0)

def AddUniqueId(builder, uniqueId):
    MiniGameShootingCharacterExcelAddUniqueId(builder, uniqueId)

def MiniGameShootingCharacterExcelAddSpineResourceName(builder, spineResourceName):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(spineResourceName), 0)

def AddSpineResourceName(builder, spineResourceName):
    MiniGameShootingCharacterExcelAddSpineResourceName(builder, spineResourceName)

def MiniGameShootingCharacterExcelAddBodyRadius(builder, bodyRadius):
    builder.PrependFloat32Slot(2, bodyRadius, 0.0)

def AddBodyRadius(builder, bodyRadius):
    MiniGameShootingCharacterExcelAddBodyRadius(builder, bodyRadius)

def MiniGameShootingCharacterExcelAddModelPrefabName(builder, modelPrefabName):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(modelPrefabName), 0)

def AddModelPrefabName(builder, modelPrefabName):
    MiniGameShootingCharacterExcelAddModelPrefabName(builder, modelPrefabName)

def MiniGameShootingCharacterExcelAddNormalAttackSkillData(builder, normalAttackSkillData):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(normalAttackSkillData), 0)

def AddNormalAttackSkillData(builder, normalAttackSkillData):
    MiniGameShootingCharacterExcelAddNormalAttackSkillData(builder, normalAttackSkillData)

def MiniGameShootingCharacterExcelAddPublicSkillData(builder, publicSkillData):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(publicSkillData), 0)

def AddPublicSkillData(builder, publicSkillData):
    MiniGameShootingCharacterExcelAddPublicSkillData(builder, publicSkillData)

def MiniGameShootingCharacterExcelStartPublicSkillDataVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPublicSkillDataVector(builder, numElems):
    return MiniGameShootingCharacterExcelStartPublicSkillDataVector(builder, numElems)

def MiniGameShootingCharacterExcelAddDeathSkillData(builder, deathSkillData):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(deathSkillData), 0)

def AddDeathSkillData(builder, deathSkillData):
    MiniGameShootingCharacterExcelAddDeathSkillData(builder, deathSkillData)

def MiniGameShootingCharacterExcelAddMaxHp(builder, maxHp):
    builder.PrependInt64Slot(7, maxHp, 0)

def AddMaxHp(builder, maxHp):
    MiniGameShootingCharacterExcelAddMaxHp(builder, maxHp)

def MiniGameShootingCharacterExcelAddAttackPower(builder, attackPower):
    builder.PrependInt64Slot(8, attackPower, 0)

def AddAttackPower(builder, attackPower):
    MiniGameShootingCharacterExcelAddAttackPower(builder, attackPower)

def MiniGameShootingCharacterExcelAddDefensePower(builder, defensePower):
    builder.PrependInt64Slot(9, defensePower, 0)

def AddDefensePower(builder, defensePower):
    MiniGameShootingCharacterExcelAddDefensePower(builder, defensePower)

def MiniGameShootingCharacterExcelAddCriticalRate(builder, criticalRate):
    builder.PrependInt64Slot(10, criticalRate, 0)

def AddCriticalRate(builder, criticalRate):
    MiniGameShootingCharacterExcelAddCriticalRate(builder, criticalRate)

def MiniGameShootingCharacterExcelAddCriticalDamageRate(builder, criticalDamageRate):
    builder.PrependInt64Slot(11, criticalDamageRate, 0)

def AddCriticalDamageRate(builder, criticalDamageRate):
    MiniGameShootingCharacterExcelAddCriticalDamageRate(builder, criticalDamageRate)

def MiniGameShootingCharacterExcelAddAttackRange(builder, attackRange):
    builder.PrependInt64Slot(12, attackRange, 0)

def AddAttackRange(builder, attackRange):
    MiniGameShootingCharacterExcelAddAttackRange(builder, attackRange)

def MiniGameShootingCharacterExcelAddMoveSpeed(builder, moveSpeed):
    builder.PrependInt64Slot(13, moveSpeed, 0)

def AddMoveSpeed(builder, moveSpeed):
    MiniGameShootingCharacterExcelAddMoveSpeed(builder, moveSpeed)

def MiniGameShootingCharacterExcelAddShotTime(builder, shotTime):
    builder.PrependInt64Slot(14, shotTime, 0)

def AddShotTime(builder, shotTime):
    MiniGameShootingCharacterExcelAddShotTime(builder, shotTime)

def MiniGameShootingCharacterExcelAddIsBoss(builder, isBoss):
    builder.PrependBoolSlot(15, isBoss, 0)

def AddIsBoss(builder, isBoss):
    MiniGameShootingCharacterExcelAddIsBoss(builder, isBoss)

def MiniGameShootingCharacterExcelAddScale(builder, scale):
    builder.PrependFloat32Slot(16, scale, 0.0)

def AddScale(builder, scale):
    MiniGameShootingCharacterExcelAddScale(builder, scale)

def MiniGameShootingCharacterExcelAddIgnoreObstacleCheck(builder, ignoreObstacleCheck):
    builder.PrependBoolSlot(17, ignoreObstacleCheck, 0)

def AddIgnoreObstacleCheck(builder, ignoreObstacleCheck):
    MiniGameShootingCharacterExcelAddIgnoreObstacleCheck(builder, ignoreObstacleCheck)

def MiniGameShootingCharacterExcelAddCharacterVoiceGroupId(builder, characterVoiceGroupId):
    builder.PrependInt64Slot(18, characterVoiceGroupId, 0)

def AddCharacterVoiceGroupId(builder, characterVoiceGroupId):
    MiniGameShootingCharacterExcelAddCharacterVoiceGroupId(builder, characterVoiceGroupId)

def MiniGameShootingCharacterExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MiniGameShootingCharacterExcelEnd(builder)
