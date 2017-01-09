class Person (val children : Vector[Person] = Vector()){
  def canKill(other : Person) = false
  def canProtect(other : Person, from : Person) = false
  def canRow = false
}

case object Man extends Person(children = Vector(ManChildA, ManChildB)) {
  override def canKill(other: Person): Boolean = other match {
    case WomanChildA | WomanChildB => true
    case _ => false
  }
  override def canProtect(other: Person, from: Person): Boolean = (other, from) match {
    case (o, Woman) => children contains o
    case _ => false
  }

  override def canRow: Boolean = true
}

case object Woman extends Person(children = Vector(WomanChildA, WomanChildB)) {
  override def canKill(other: Person): Boolean = other match {
    case ManChildA | ManChildB => true
    case _ => false
  }

  override def canProtect(other: Person, from: Person): Boolean = (other, from) match {
    case (o, Man) => children contains o
    case _ => false
  }
  override def canRow: Boolean = true

}

case object ManChildA extends Person()

case object ManChildB extends Person()

case object WomanChildA extends Person()

case object WomanChildB extends Person()

case object Hunter extends Person() {
  override def canProtect(other: Person, from: Person): Boolean = (other, from) match {
    case (_, Werewolf) => true
    case _ => false
  }
  override def canRow: Boolean = true
}

case object Werewolf extends Person() {
  override def canKill(other: Person): Boolean = other != Hunter
}

case object Wolf extends Person() {
  override def canKill(other: Person): Boolean = other match {
    case Sheep => true
    case _ => false
  }
}

case object Veg extends Person()

case object Sheep extends Person() {
  override def canKill(other: Person): Boolean = other match {
    case Veg => true
    case _ => false
  }
}

case object FerryMan extends Person() {
  override def canProtect(other: Person, from: Person): Boolean = (other, from) match {
    case (Sheep, Wolf) => true
    case (Veg, Sheep) => true
  }

  override def canRow: Boolean = true
}
