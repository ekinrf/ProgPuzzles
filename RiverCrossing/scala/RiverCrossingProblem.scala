
class RiverCrossingProblem(val initState : WorldState, targetState : WorldState) {
  require(initState isSafe, "Initial state must be safe.")

  class Path(val history : List[WorldState]) {
    def currentState: WorldState = history.head

    override def toString: String = history.reverse.mkString("\n") + "\n ---------------END---------------"
  }

  def explore(paths : Set[Path]) : Stream[Path] = {
    val newPaths = for {
      path <- paths
      newState <- path.currentState.nextStates
      if !path.history.contains(newState) && newState.isSafe
    } yield new Path(newState :: path.history)
    if(newPaths.isEmpty) Stream()
    else newPaths.toStream append explore(newPaths)
  }

  def exploreDFS(paths : List[Path]) : Stream[Path] =  paths match {
    case path :: tail =>
      val newStates = path.currentState.nextStates.filter(_.isSafe).diff(path.history.toSet)
      val newPaths = newStates.map(state => new Path(state :: path.history))
      newPaths.toStream append exploreDFS(newPaths.toList ++ tail)

    case Nil => Stream()
  }

  def solutions : Stream[Path] = for {
    path <- explore(Set(new Path(List(initState))))
    if path.currentState == targetState
  } yield path

  def solutionsDFS : Stream[Path] = for {
    path <- exploreDFS(List(new Path(List(initState))))
    if path.currentState == targetState
  } yield path
}
