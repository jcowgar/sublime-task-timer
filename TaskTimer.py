from datetime import datetime
import sublime, sublime_plugin


class TaskTimerStartCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        sublime.task_timer_time = datetime.now()


class TaskTimerStatusCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        try:
            td = datetime.now() - sublime.task_timer_time
            seconds = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60

            output = []
            if hours > 1:
                output.append('%i hours' % hours)
            elif hours == 1:
                output.append('1 hour')
            if minutes > 1:
                output.append('%i minutes' % minutes)
            elif minutes == 1:
                output.append('1 minute')
            if seconds > 1:
                output.append('%i seconds' % seconds)
            elif seconds == 1:
                output.append('1 second')

            sublime.status_message(' '.join(output))
        except:
            sublime.status_message('task timer not running')
