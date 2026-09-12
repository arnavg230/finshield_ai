from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse
)


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post(
    "/",
    response_model=TransactionResponse
)
def create_transaction(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    transaction = Transaction(
        user_id=current_user.id,
        sender=transaction_data.sender,
        receiver=transaction_data.receiver,
        transaction_type=transaction_data.transaction_type,
        amount=transaction_data.amount,
        timestamp=transaction_data.timestamp,
        status="pending"
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


@router.get(
    "/",
    response_model=list[TransactionResponse]
)
def get_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()

    return transactions


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.user_id == current_user.id
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction