import sublime
import sublime_plugin
import subprocess

class OpenInEmacsCommand(sublime_plugin.WindowCommand):
    def run(self):
        emacsclient = "/usr/local/bin/emacsclient"
        option = "-n"
        path = None

        if self.window.active_view():
            path = "\"" + self.window.active_view().file_name() + "\""
        else:
            sublime.error_message(__name__ + ": No file to open.")
            return

        full_cmd = " ".join([emacsclient, option, path])
        subprocess.call(full_cmd, shell=True)
