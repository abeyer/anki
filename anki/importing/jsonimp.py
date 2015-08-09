# -*- coding: utf-8 -*-
# Copyright: Andrew Beyer <beyer.andrew@gmail.com>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import json

from anki.importing.noteimp import NoteImporter, ForeignNote
from anki.lang import _


class JSONImporter(NoteImporter):

    def __init__(self, *args):
        NoteImporter.__init__(self, *args)
        self.fileobj = None

    def foreignNotes(self):
        self.open()
        notes = []
        for row in self.data:
            if len(row) != self.numFields:
                continue
            note = self.noteFromFields(row)
            notes.append(note)
        self.fileobj.close()
        return notes

    def open(self):
        self.cacheFile()

    def cacheFile(self):
        if not self.fileobj:
            self.openFile()

    def openFile(self):
        self.fileobj = open(self.file, "rbU")
        self.data = json.load(self.fileobj)
        self.numFields = len(self.data[0]) if self.data else 0

    def fields(self):
        self.open()
        return self.numFields

    def noteFromFields(self, fields):
        note = ForeignNote()
        note.fields.extend([x for x in fields])
        return note
