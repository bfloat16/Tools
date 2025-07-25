# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterSkillListExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterSkillListExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterSkillListExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterSkillListExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterSkillListExcel
    def CharacterSkillListGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterSkillListExcel
    def MinimumGradeCharacterWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterSkillListExcel
    def MinimumTierCharacterGear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterSkillListExcel
    def FormIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterSkillListExcel
    def IsRootMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterSkillListExcel
    def IsMoveLeftRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterSkillListExcel
    def UseRandomExSkillTimeline(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # CharacterSkillListExcel
    def TsainteractionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterSkillListExcel
    def NormalSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def NormalSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def NormalSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # CharacterSkillListExcel
    def NormalSkillTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterSkillListExcel
    def NormalSkillTimeLineIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterSkillListExcel
    def NormalSkillTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def NormalSkillTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # CharacterSkillListExcel
    def ExSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def ExSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def ExSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # CharacterSkillListExcel
    def ExSkillCutInTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def ExSkillCutInTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def ExSkillCutInTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # CharacterSkillListExcel
    def ExSkillLevelTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def ExSkillLevelTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def ExSkillLevelTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # CharacterSkillListExcel
    def PublicSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def PublicSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def PublicSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # CharacterSkillListExcel
    def PublicSkillTimeLineIndex(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CharacterSkillListExcel
    def PublicSkillTimeLineIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CharacterSkillListExcel
    def PublicSkillTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def PublicSkillTimeLineIndexIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # CharacterSkillListExcel
    def PassiveSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def PassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def PassiveSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

    # CharacterSkillListExcel
    def LeaderSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def LeaderSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def LeaderSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0

    # CharacterSkillListExcel
    def ExtraPassiveSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def ExtraPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def ExtraPassiveSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

    # CharacterSkillListExcel
    def HiddenPassiveSkillGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CharacterSkillListExcel
    def HiddenPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterSkillListExcel
    def HiddenPassiveSkillGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0

def CharacterSkillListExcelStart(builder):
    builder.StartObject(19)

def Start(builder):
    CharacterSkillListExcelStart(builder)

def CharacterSkillListExcelAddCharacterSkillListGroupId(builder, characterSkillListGroupId):
    builder.PrependInt64Slot(0, characterSkillListGroupId, 0)

def AddCharacterSkillListGroupId(builder, characterSkillListGroupId):
    CharacterSkillListExcelAddCharacterSkillListGroupId(builder, characterSkillListGroupId)

def CharacterSkillListExcelAddMinimumGradeCharacterWeapon(builder, minimumGradeCharacterWeapon):
    builder.PrependInt32Slot(1, minimumGradeCharacterWeapon, 0)

def AddMinimumGradeCharacterWeapon(builder, minimumGradeCharacterWeapon):
    CharacterSkillListExcelAddMinimumGradeCharacterWeapon(builder, minimumGradeCharacterWeapon)

def CharacterSkillListExcelAddMinimumTierCharacterGear(builder, minimumTierCharacterGear):
    builder.PrependInt32Slot(2, minimumTierCharacterGear, 0)

def AddMinimumTierCharacterGear(builder, minimumTierCharacterGear):
    CharacterSkillListExcelAddMinimumTierCharacterGear(builder, minimumTierCharacterGear)

def CharacterSkillListExcelAddFormIndex(builder, formIndex):
    builder.PrependInt32Slot(3, formIndex, 0)

def AddFormIndex(builder, formIndex):
    CharacterSkillListExcelAddFormIndex(builder, formIndex)

def CharacterSkillListExcelAddIsRootMotion(builder, isRootMotion):
    builder.PrependBoolSlot(4, isRootMotion, 0)

def AddIsRootMotion(builder, isRootMotion):
    CharacterSkillListExcelAddIsRootMotion(builder, isRootMotion)

def CharacterSkillListExcelAddIsMoveLeftRight(builder, isMoveLeftRight):
    builder.PrependBoolSlot(5, isMoveLeftRight, 0)

def AddIsMoveLeftRight(builder, isMoveLeftRight):
    CharacterSkillListExcelAddIsMoveLeftRight(builder, isMoveLeftRight)

def CharacterSkillListExcelAddUseRandomExSkillTimeline(builder, useRandomExSkillTimeline):
    builder.PrependBoolSlot(6, useRandomExSkillTimeline, 0)

def AddUseRandomExSkillTimeline(builder, useRandomExSkillTimeline):
    CharacterSkillListExcelAddUseRandomExSkillTimeline(builder, useRandomExSkillTimeline)

def CharacterSkillListExcelAddTsainteractionId(builder, tsainteractionId):
    builder.PrependInt64Slot(7, tsainteractionId, 0)

def AddTsainteractionId(builder, tsainteractionId):
    CharacterSkillListExcelAddTsainteractionId(builder, tsainteractionId)

def CharacterSkillListExcelAddNormalSkillGroupId(builder, normalSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(normalSkillGroupId), 0)

def AddNormalSkillGroupId(builder, normalSkillGroupId):
    CharacterSkillListExcelAddNormalSkillGroupId(builder, normalSkillGroupId)

def CharacterSkillListExcelStartNormalSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartNormalSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartNormalSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelAddNormalSkillTimeLineIndex(builder, normalSkillTimeLineIndex):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(normalSkillTimeLineIndex), 0)

def AddNormalSkillTimeLineIndex(builder, normalSkillTimeLineIndex):
    CharacterSkillListExcelAddNormalSkillTimeLineIndex(builder, normalSkillTimeLineIndex)

def CharacterSkillListExcelStartNormalSkillTimeLineIndexVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartNormalSkillTimeLineIndexVector(builder, numElems):
    return CharacterSkillListExcelStartNormalSkillTimeLineIndexVector(builder, numElems)

def CharacterSkillListExcelAddExSkillGroupId(builder, exSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(exSkillGroupId), 0)

def AddExSkillGroupId(builder, exSkillGroupId):
    CharacterSkillListExcelAddExSkillGroupId(builder, exSkillGroupId)

def CharacterSkillListExcelStartExSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartExSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartExSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelAddExSkillCutInTimeLineIndex(builder, exSkillCutInTimeLineIndex):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(exSkillCutInTimeLineIndex), 0)

def AddExSkillCutInTimeLineIndex(builder, exSkillCutInTimeLineIndex):
    CharacterSkillListExcelAddExSkillCutInTimeLineIndex(builder, exSkillCutInTimeLineIndex)

def CharacterSkillListExcelStartExSkillCutInTimeLineIndexVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartExSkillCutInTimeLineIndexVector(builder, numElems):
    return CharacterSkillListExcelStartExSkillCutInTimeLineIndexVector(builder, numElems)

def CharacterSkillListExcelAddExSkillLevelTimeLineIndex(builder, exSkillLevelTimeLineIndex):
    builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(exSkillLevelTimeLineIndex), 0)

def AddExSkillLevelTimeLineIndex(builder, exSkillLevelTimeLineIndex):
    CharacterSkillListExcelAddExSkillLevelTimeLineIndex(builder, exSkillLevelTimeLineIndex)

def CharacterSkillListExcelStartExSkillLevelTimeLineIndexVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartExSkillLevelTimeLineIndexVector(builder, numElems):
    return CharacterSkillListExcelStartExSkillLevelTimeLineIndexVector(builder, numElems)

def CharacterSkillListExcelAddPublicSkillGroupId(builder, publicSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(publicSkillGroupId), 0)

def AddPublicSkillGroupId(builder, publicSkillGroupId):
    CharacterSkillListExcelAddPublicSkillGroupId(builder, publicSkillGroupId)

def CharacterSkillListExcelStartPublicSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPublicSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartPublicSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelAddPublicSkillTimeLineIndex(builder, publicSkillTimeLineIndex):
    builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(publicSkillTimeLineIndex), 0)

def AddPublicSkillTimeLineIndex(builder, publicSkillTimeLineIndex):
    CharacterSkillListExcelAddPublicSkillTimeLineIndex(builder, publicSkillTimeLineIndex)

def CharacterSkillListExcelStartPublicSkillTimeLineIndexVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPublicSkillTimeLineIndexVector(builder, numElems):
    return CharacterSkillListExcelStartPublicSkillTimeLineIndexVector(builder, numElems)

def CharacterSkillListExcelAddPassiveSkillGroupId(builder, passiveSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(passiveSkillGroupId), 0)

def AddPassiveSkillGroupId(builder, passiveSkillGroupId):
    CharacterSkillListExcelAddPassiveSkillGroupId(builder, passiveSkillGroupId)

def CharacterSkillListExcelStartPassiveSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPassiveSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartPassiveSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelAddLeaderSkillGroupId(builder, leaderSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(leaderSkillGroupId), 0)

def AddLeaderSkillGroupId(builder, leaderSkillGroupId):
    CharacterSkillListExcelAddLeaderSkillGroupId(builder, leaderSkillGroupId)

def CharacterSkillListExcelStartLeaderSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartLeaderSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartLeaderSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelAddExtraPassiveSkillGroupId(builder, extraPassiveSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(extraPassiveSkillGroupId), 0)

def AddExtraPassiveSkillGroupId(builder, extraPassiveSkillGroupId):
    CharacterSkillListExcelAddExtraPassiveSkillGroupId(builder, extraPassiveSkillGroupId)

def CharacterSkillListExcelStartExtraPassiveSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartExtraPassiveSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartExtraPassiveSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelAddHiddenPassiveSkillGroupId(builder, hiddenPassiveSkillGroupId):
    builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(hiddenPassiveSkillGroupId), 0)

def AddHiddenPassiveSkillGroupId(builder, hiddenPassiveSkillGroupId):
    CharacterSkillListExcelAddHiddenPassiveSkillGroupId(builder, hiddenPassiveSkillGroupId)

def CharacterSkillListExcelStartHiddenPassiveSkillGroupIdVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartHiddenPassiveSkillGroupIdVector(builder, numElems):
    return CharacterSkillListExcelStartHiddenPassiveSkillGroupIdVector(builder, numElems)

def CharacterSkillListExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return CharacterSkillListExcelEnd(builder)
