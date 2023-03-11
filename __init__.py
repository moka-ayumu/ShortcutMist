# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ShortcutMist",
    "author" : "MOKA AYUMU",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "3D VIEW"
}

import bpy

addon_keymaps = []

def menu_func(self, context):
    self.layout.operator(MistOperator.bl_idname, text="Toggle Mist")

def register():
    bpy.utils.register_class(MistOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')

    kmi = km.keymap_items.new(MistOperator.bl_idname, 'END', 'PRESS', ctrl=True, shift=False)

    addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    bpy.utils.unregister_class(MistOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    addon_keymaps.clear()

if  __name__ == "__main__":
    register()

class MistOperator(bpy.types.Operator):
    bl_idname = "wm.mist"
    bl_label = "Toggle Mist"

    def execute(self, context):
        if context.space_data.shading.render_pass == 'MIST':
            context.space_data.shading.render_pass = 'COMBINED'
        else:
            context.space_data.shading.render_pass = 'MIST'
        return {'FINISHED'}