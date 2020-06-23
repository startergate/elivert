from drf_yasg import openapi

SessionKey = openapi.Schema(
    '세션 키',
    description='세션 키',
    type=openapi.TYPE_STRING
)

SessionCreateSuccessful = openapi.Schema(
    '세션 생성됨',
    type=openapi.TYPE_OBJECT,
    properties={
        'session': SessionKey
    }
)
