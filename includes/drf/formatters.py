from dataclasses import asdict

from drf_standardized_errors.formatter import ExceptionFormatter
from drf_standardized_errors.types import ErrorResponse


class APIExceptionFormatter(ExceptionFormatter):
    def format_error_response(self, error_response: ErrorResponse):
        error = error_response.errors[0]
        errors = asdict(error_response)["errors"]
        if (
            error_response.type == "validation_error"
            and error.attr != "non_field_errors"
            and error.attr is not None
        ):
            error_message = f"{error.attr}: {error.detail}"
        else:
            error_message = error.detail
        return {
            "success": False,
            "message": error_message,
            "details": errors,
        }