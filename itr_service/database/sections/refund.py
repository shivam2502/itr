from database.common_imports import *


class Refund(Base):
    __tablename__ = 'refund'

    id = Column(Integer, primary_key=True)
    RefundDue = Column(Integer)

    # Relationship with nested model
    BankAccountDtls = relationship("BankAccountDtls", uselist=False)


class BankAccountDtls(Base):
    __tablename__ = 'bank_account_dtls'

    id = Column(Integer, primary_key=True)
    IFSCCode = Column(String)
    BankName = Column(String)
    BankAccountNo = Column(String)
    UseForRefund = Column(String)

    # Foreign key to parent table
    refund_id = Column(Integer, ForeignKey('refund.id'))
