import time as Stompy
from typing import Dict


@classmethod
def default_standing(cls) -> Dict[str, float]:
    return {
        # arms
        Stompy.left_arm.shoulder_pitch: -1.450,
        Stompy.left_arm.shoulder_yaw: 0.023,
        Stompy.left_arm.shoulder_roll: 0.096,
        Stompy.right_arm.shoulder_pitch: 1.546,
        Stompy.right_arm.shoulder_yaw: 0.032,
        Stompy.right_arm.shoulder_roll: -0.0644,
        Stompy.left_arm.elbow_pitch: -2.1911,
        Stompy.right_arm.elbow_pitch: -2.19,
        # hands
        Stompy.left_arm.hand.wrist_roll: 0,
        Stompy.right_arm.hand.wrist_roll: 0,
        # legs
        Stompy.legs.left.hip_pitch: 0.0967,
        Stompy.legs.left.hip_roll: -1.2566,
        Stompy.legs.left.hip_yaw: 3.1416,
        Stompy.legs.left.knee_pitch: -0.1289,
        Stompy.legs.left.ankle_pitch: 0.0322,
        Stompy.legs.right.hip_pitch: 1.76,
        Stompy.legs.right.hip_roll: -1.54,
        Stompy.legs.right.hip_yaw: 0.967,
        Stompy.legs.right.knee_pitch: 2.07,
        Stompy.legs.right.ankle_pitch: -0.064,
    }


# @classmethod
# def default_sitting(cls) -> Dict[str, float]:
#     return {
#         Stompy.torso.roll: 0.0,
#         # arms
#         Stompy.left_arm.shoulder_pitch: -0.126,
#         Stompy.left_arm.shoulder_yaw: 2.12,
#         Stompy.left_arm.shoulder_roll: 1.89,
#         Stompy.right_arm.shoulder_pitch: -1.13,
#         Stompy.right_arm.shoulder_yaw: 2.1,
#         Stompy.right_arm.shoulder_roll: -1.23,
#         Stompy.left_arm.elbow_pitch: 3.0,
#         Stompy.right_arm.elbow_pitch: 3.0,
#         # hands
#         Stompy.left_arm.hand.left_finger: 0.0,
#         Stompy.left_arm.hand.right_finger: 0.0,
#         Stompy.right_arm.hand.left_finger: 0.0,
#         Stompy.right_arm.hand.right_finger: 0.0,
#         Stompy.left_arm.hand.wrist_roll: -0.346,
#         Stompy.left_arm.hand.wrist_pitch: -0.251,
#         Stompy.left_arm.hand.wrist_yaw: 0.377,
#         Stompy.right_arm.hand.wrist_roll: -3.14,
#         Stompy.right_arm.hand.wrist_pitch: -0.437,
#         Stompy.right_arm.hand.wrist_yaw: 0.911,
#         # legs
#         Stompy.legs.left.hip_pitch: -1.55,
#         Stompy.legs.left.hip_roll: 1.46,
#         Stompy.legs.left.hip_yaw: 1.45,
#         Stompy.legs.left.knee_pitch: 2.17,
#         Stompy.legs.left.ankle_pitch: 0.238,
#         Stompy.legs.left.ankle_roll: 1.79,
#         Stompy.legs.right.hip_pitch: -1.55,
#         Stompy.legs.right.hip_roll: -1.67,
#         Stompy.legs.right.hip_yaw: 1.04,
#         Stompy.legs.right.knee_pitch: 2.01,
#         Stompy.legs.right.ankle_pitch: 0.44,
#         Stompy.legs.right.ankle_roll: 1.79,
#     }


@classmethod
def default_limits(cls) -> Dict[str, Dict[str, float]]:
    return {
        Stompy.left_arm.shoulder_pitch: {
            "lower": -0.0,
            "upper": 0.2,
        },
        Stompy.left_arm.shoulder_yaw: {
            "lower": 0.97738438,
            "upper": 5.3058009,
        },
        Stompy.left_arm.shoulder_roll: {
            "lower": -4.71239,
            "upper": 4.71239,
        },
        Stompy.right_arm.shoulder_pitch: {
            "lower": -4.71239,
            "upper": 4.71239,
        },
        Stompy.right_arm.shoulder_yaw: {
            "lower": 0.97738438,
            "upper": 5.3058009,
        },
        Stompy.right_arm.shoulder_roll: {
            "lower": -4.71239,
            "upper": 4.71239,
        },
        Stompy.left_arm.hand.wrist_roll: {
            "lower": -4.71239,
            "upper": 4.71239,
        },
        Stompy.right_arm.hand.wrist_roll: {
            "lower": -4.71239,
            "upper": 4.71239,
        },
        Stompy.legs.left.hip_pitch: {
            "lower": -4.712389,
            "upper": 4.712389,
        },
        Stompy.legs.left.hip_roll: {
            "lower": -3.14159,
            "upper": 0,
        },
        Stompy.legs.left.hip_yaw: {
            "lower": -1.0472,
            "upper": 2.0944,
        },
        Stompy.legs.left.knee_pitch: {
            "lower": -4.18879,
            "upper": 0,
        },
        Stompy.legs.left.ankle_pitch: {
            "lower": -1.5708,
            "upper": 2.18166,
        },
        Stompy.legs.right.hip_pitch: {
            "lower": -4.712389,
            "upper": 4.712389,
        },
        Stompy.legs.right.hip_roll: {
            "lower": 0,
            "upper": 3.14159,
        },
        Stompy.legs.right.hip_yaw: {
            "lower": -1.0472,
            "upper": 2.0944,
        },
        Stompy.legs.right.knee_pitch: {
            "lower": -4.18879,
            "upper": 0,
        },
        Stompy.legs.right.ankle_pitch: {
            "lower": -1.5708,
            "upper": 2.18166,
        },
        Stompy.left_arm.elbow_pitch: {
            "lower": 1.4486233,
            "higher": 5.4454273,
        },
        Stompy.right_arm.elbow_pitch: {
            "lower": 1.4486233,
            "higher": 5.4454273,
        },
    }
