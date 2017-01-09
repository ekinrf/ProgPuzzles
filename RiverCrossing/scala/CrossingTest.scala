object CrossingTest extends App{

  def time[A](f: => A): A = {
    val s = System.nanoTime
    val ret = f
    println("time elapsed: "+(System.nanoTime-s)/1e6+"ms")
    ret
  }

  val init = new WorldState(Set(Man, Woman, ManChildA, ManChildB, WomanChildA, WomanChildB, Werewolf, Hunter), Set(), boatAtOriBank = true)
  val target = new WorldState(Set(), Set(Man, Woman, ManChildA, ManChildB, WomanChildA, WomanChildB, Werewolf, Hunter), boatAtOriBank = false)
  val problem = new RiverCrossingProblem(init, target)
  time{problem.solutions.take(2)}.foreach(println)
  time{problem.solutionsDFS.take(2)}.foreach(println)

  val init2 = new WorldState(Set(FerryMan, Sheep, Wolf, Veg), Set(), boatAtOriBank = true)
  val target2 = new WorldState(Set(), Set(FerryMan, Sheep, Wolf, Veg), boatAtOriBank = false)
  val problem2 = new RiverCrossingProblem(init2, target2)
  time{problem2.solutions.take(10)}.foreach(println)
}

