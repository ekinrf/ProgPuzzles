case class Memo[A1, A2, B](f : (A1, A2) => B) {
  val cache = collection.mutable.HashMap[(A1, A2), B]().empty
  def apply(a1 : A1, a2 :A2): B = cache.getOrElseUpdate((a1, a2), f(a1, a2));
}

object StringEditDistance extends  App {

  lazy val ED : Memo[List[Char], List[Char], Int] = Memo {
    case (Nil, tar) => tar.length
    case (ori, Nil) => ori.length

    case (oriHead :: oriTail, tarHead :: tarTail) =>
      val editOp = {
        if(oriHead == tarHead) ED(oriTail, tarTail)
        else 1 + ED(oriTail, tarTail)
      }
      val delOp = 1 + ED(oriTail, tarHead :: tarTail)
      val addOp = 1 + ED(oriHead :: oriTail, tarTail)

      Math.min(Math.min(editOp, delOp), addOp)
  }

  def calEditDistance(original : String, target : String): Int = ED(original.toList, target.toList);

  //Test
  println(calEditDistance("siiittking", "sitting"))
  println(calEditDistance("kitten", "sitting"))
  println(calEditDistance("intention", "execution"))
}
