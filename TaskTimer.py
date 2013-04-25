from datetime import datetime

import sublime
from sublime_plugin import ApplicationCommand


def increment_seconds():
    if sublime.task_timer_time is not None:
        td = datetime.now() - sublime.task_timer_time
        sublime.task_timer_seconds += (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6) / 10 ** 6


def report_time():
    has_run = hasattr(sublime, 'task_timer_seconds')
    if has_run is False or (has_run and sublime.task_timer_seconds == 0):
        sublime.status_message('task timer not running')
        return

    seconds = sublime.task_timer_seconds

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


class TaskTimerStartCommand(ApplicationCommand):
    def run(self):
        if not hasattr(sublime, 'task_timer_seconds'):
            sublime.task_timer_seconds = 0
        sublime.task_timer_time = datetime.now()


class TaskTimerPauseCommand(ApplicationCommand):
    """A sublime text command to pause the timer"""
    def run(self):
        try:
            increment_seconds()

            report_time()

            sublime.task_timer_time = None

        except:
            sublime.status_message("task timer not running")


class TaskTimerStopCommand(ApplicationCommand):
    """A sublime text command to stop the timer"""
    def run(self):
        increment_seconds()

        report_time()

        sublime.task_timer_seconds = 0
        sublime.task_timer_time = None


class TaskTimerStatusCommand(ApplicationCommand):
    def run(self):
        increment_seconds()

        report_time()

        if sublime.task_timer_time is not None:
            sublime.task_timer_time = datetime.now()
