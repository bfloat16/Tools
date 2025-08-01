# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameDreamTimelineExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameDreamTimelineExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMiniGameDreamTimelineExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MiniGameDreamTimelineExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameDreamTimelineExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def DreamMakerDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def DreamMakerActionPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def EnterScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def Bgm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameDreamTimelineExcel
    def ArtLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameDreamTimelineExcel
    def DesignLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def MiniGameDreamTimelineExcelStart(builder):
    builder.StartObject(9)

def Start(builder):
    MiniGameDreamTimelineExcelStart(builder)

def MiniGameDreamTimelineExcelAddId(builder, id):
    builder.PrependInt64Slot(0, id, 0)

def AddId(builder, id):
    MiniGameDreamTimelineExcelAddId(builder, id)

def MiniGameDreamTimelineExcelAddEventContentId(builder, eventContentId):
    builder.PrependInt64Slot(1, eventContentId, 0)

def AddEventContentId(builder, eventContentId):
    MiniGameDreamTimelineExcelAddEventContentId(builder, eventContentId)

def MiniGameDreamTimelineExcelAddGroupId(builder, groupId):
    builder.PrependInt64Slot(2, groupId, 0)

def AddGroupId(builder, groupId):
    MiniGameDreamTimelineExcelAddGroupId(builder, groupId)

def MiniGameDreamTimelineExcelAddDreamMakerDays(builder, dreamMakerDays):
    builder.PrependInt64Slot(3, dreamMakerDays, 0)

def AddDreamMakerDays(builder, dreamMakerDays):
    MiniGameDreamTimelineExcelAddDreamMakerDays(builder, dreamMakerDays)

def MiniGameDreamTimelineExcelAddDreamMakerActionPoint(builder, dreamMakerActionPoint):
    builder.PrependInt64Slot(4, dreamMakerActionPoint, 0)

def AddDreamMakerActionPoint(builder, dreamMakerActionPoint):
    MiniGameDreamTimelineExcelAddDreamMakerActionPoint(builder, dreamMakerActionPoint)

def MiniGameDreamTimelineExcelAddEnterScenarioGroupId(builder, enterScenarioGroupId):
    builder.PrependInt64Slot(5, enterScenarioGroupId, 0)

def AddEnterScenarioGroupId(builder, enterScenarioGroupId):
    MiniGameDreamTimelineExcelAddEnterScenarioGroupId(builder, enterScenarioGroupId)

def MiniGameDreamTimelineExcelAddBgm(builder, bgm):
    builder.PrependInt64Slot(6, bgm, 0)

def AddBgm(builder, bgm):
    MiniGameDreamTimelineExcelAddBgm(builder, bgm)

def MiniGameDreamTimelineExcelAddArtLevelPath(builder, artLevelPath):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(artLevelPath), 0)

def AddArtLevelPath(builder, artLevelPath):
    MiniGameDreamTimelineExcelAddArtLevelPath(builder, artLevelPath)

def MiniGameDreamTimelineExcelAddDesignLevelPath(builder, designLevelPath):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(designLevelPath), 0)

def AddDesignLevelPath(builder, designLevelPath):
    MiniGameDreamTimelineExcelAddDesignLevelPath(builder, designLevelPath)

def MiniGameDreamTimelineExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MiniGameDreamTimelineExcelEnd(builder)
