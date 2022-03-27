from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')

def validate_file_max_size(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError('Max file size is %sMB' % str(max_size))
    return validate


# class MaxFileSizeValidator:
#     def __init__(self, max_size):
#         self.max_size = max_size
#     def __call__(self, value):
#         filesize = value.file.size
#         if filesize > self.__megabytes_to_bytes(self.max_size):
#             raise ValidationError(self.__get_exception_message())
#
#     def __megabytes_to_bytes(self, value):
#         return value * 1024 * 1024
#     def __get_exception_message(self):
#         return f'Max file size is {self.max_size:.2f} MB'