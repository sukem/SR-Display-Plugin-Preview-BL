# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SetAnimationFrameCommand(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SetAnimationFrameCommand()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSetAnimationFrameCommand(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SetAnimationFrameCommand
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SetAnimationFrameCommand
    def Frame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SetAnimationFrameCommand
    def Fps(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(2)
def SetAnimationFrameCommandStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFrame(builder, frame): builder.PrependInt32Slot(0, frame, 0)
def SetAnimationFrameCommandAddFrame(builder, frame):
    """This method is deprecated. Please switch to AddFrame."""
    return AddFrame(builder, frame)
def AddFps(builder, fps): builder.PrependFloat32Slot(1, fps, 0.0)
def SetAnimationFrameCommandAddFps(builder, fps):
    """This method is deprecated. Please switch to AddFps."""
    return AddFps(builder, fps)
def End(builder): return builder.EndObject()
def SetAnimationFrameCommandEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)