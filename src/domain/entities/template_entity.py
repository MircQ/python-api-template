import uuid

from pydantic import BaseModel, UUID4, Field


class TemplateEntity(BaseModel):

    """

    """

    id: UUID4 = Field(
        title="id",
        description="Id of the entity",
        default_factory=uuid.uuid4
    )

    description: str = Field(
        title="description",
        description="Description of the entity"
    )