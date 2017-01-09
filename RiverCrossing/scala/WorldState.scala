class WorldState(val oriBank : Set[Person], val dstBank : Set[Person], val boatAtOriBank : Boolean){
  type State = Set[Person]

  private def isStateSafe(state : State) : Boolean ={
    def willKill(attacker : Person, victim : Person) = {
      (attacker canKill victim) && !(state exists (person => person.canProtect(victim, attacker)))
    }
    !state.exists(attacker => state.diff(Set(attacker)).exists(victim => willKill(attacker, victim)))
  }

  private def move(from : State, to : State, fromOriToDst : Boolean) : Set[WorldState] = {
    val twoPMove = for {
      p1 <- from
      p2 <- from
      if p1 != p2 && p1.canRow && isStateSafe(Set(p1, p2))
    } yield
      if(fromOriToDst) new WorldState(from.filterNot(_ == p1).filterNot(_ == p2), to + p1 + p2, !boatAtOriBank)
      else new WorldState(to + p1 + p2, from.filterNot(_ == p1).filterNot(_ == p2), !boatAtOriBank)
    val onePMove = from.filter(_.canRow).map(person => {
      if(fromOriToDst) new WorldState(from.filterNot(_ == person), to +person, !boatAtOriBank)
      else new WorldState(to + person, from.filterNot(_ == person), !boatAtOriBank)
    })
    onePMove ++ twoPMove
  }

  def nextStates : Set[WorldState] = if(boatAtOriBank) move(oriBank, dstBank, fromOriToDst = true) else move(dstBank, oriBank, fromOriToDst = false)

  def isSafe : Boolean = isStateSafe(oriBank) && isStateSafe(dstBank)

  override def equals(obj: scala.Any): Boolean = obj match {
    case obj : WorldState => oriBank == obj.oriBank && dstBank == obj.dstBank && boatAtOriBank == obj.boatAtOriBank
    case _ => false
  }

  override def hashCode(): Int = dstBank.hashCode

  override def toString: String = "original: " + oriBank + " dest: " + dstBank + " boat at " + {if(boatAtOriBank) "ori" else "dst"}
}
