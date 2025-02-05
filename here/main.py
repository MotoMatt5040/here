import traceback


class Here:
    def __str__(self):
        stack = traceback.extract_stack()
        caller_frame = stack[-2]

        if caller_frame.name == '<module>':
            return f"{caller_frame.filename} - line {caller_frame.lineno}"
        return f"{caller_frame.filename} - line {caller_frame.lineno}"


here = Here()
